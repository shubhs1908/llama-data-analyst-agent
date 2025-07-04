import os
import pandas as pd
import fitz  # PyMuPDF
import docx
from PIL import Image
import pytesseract
import together
import matplotlib.pyplot as plt
import seaborn as sns

# === USER MUST SET THIS ===
together.api_key = "YPUR-API-KEY"
MODEL = "meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8"

def ask_llama(prompt):
    print("\n🔍 Asking LLaMA...")
    response = together.Complete.create(
        model=MODEL,
        prompt=prompt,
        max_tokens=512,
        temperature=0.7,
        top_k=50,
        top_p=0.95,
        repetition_penalty=1.1,
    )
    return response['output']['choices'][0]['text'].strip()

def extract_text_from_file(file_path):
    ext = file_path.split('.')[-1].lower()

    if ext == 'csv':
        return pd.read_csv(file_path)
    elif ext == 'xlsx':
        return pd.read_excel(file_path)
    elif ext == 'txt':
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    elif ext == 'docx':
        doc = docx.Document(file_path)
        return '\n'.join([p.text for p in doc.paragraphs])
    elif ext == 'pdf':
        doc = fitz.open(file_path)
        return "\n".join([page.get_text() for page in doc])
    elif ext in ['jpg', 'jpeg', 'png']:
        return pytesseract.image_to_string(Image.open(file_path))
    else:
        return "Unsupported file format"

def visualize_data(df):
    numeric = df.select_dtypes(include='number')
    if numeric.shape[1] >= 2:
        x, y = numeric.columns[:2]
        sns.scatterplot(data=df, x=x, y=y)
        plt.title(f"Scatter plot: {x} vs {y}")
        plt.show()
    elif numeric.shape[1] == 1:
        col = numeric.columns[0]
        sns.histplot(df[col], kde=True)
        plt.title(f"Histogram of {col}")
        plt.show()
    else:
        print("No numeric columns found for plotting.")

def main():
    print("📊 Data Analyst Agent (LLaMA-4 Maverick)")
    file_path = input("Enter full path to your file (.csv, .xlsx, .pdf, .txt, .docx, .png, .jpg): ").strip()

    if not os.path.exists(file_path):
        print("❌ File not found. Exiting.")
        return

    content = extract_text_from_file(file_path)

    if isinstance(content, pd.DataFrame):
        print("\n✅ Loaded structured data.")
        print("\nData preview:\n", content.head())
        print("\nData description:\n", content.describe())

        try:
            visualize_data(content)
        except Exception as e:
            print("⚠️ Visualization error:", e)

        while True:
            question = input("\nAsk a question about the data (or type 'exit' to stop): ")
            if question.lower() == 'exit':
                break
            prompt = f"You are a data analyst. Based on the following data:\n{content.head(10).to_string()}\n\nAnswer the question: {question}"
            print("\n💬 LLaMA's Answer:", ask_llama(prompt))

    elif isinstance(content, str):
        print("\n✅ Loaded unstructured text.")
        print("\nText preview:\n", content[:500])

        while True:
            question = input("\nAsk a question about the text (or type 'exit' to stop): ")
            if question.lower() == 'exit':
                break
            prompt = f"The following is a document:\n{content[:1000]}\n\nQuestion: {question}"
            print("\n💬 LLaMA's Answer:", ask_llama(prompt))
    else:
        print("❌ Could not process the file.")

if __name__ == "__main__":
    main()
