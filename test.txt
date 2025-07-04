import together
import os

# Set your Together API key
os.environ["TOGETHER_API_KEY"] = "tgp_v1_M3j9QipclGLurRzixDHas-Ab18Fl2qi2P2RRqjdmDas"

MODEL = "meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8"

response = together.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of India?"}
    ],
    max_tokens=50
)

print("✅ LLaMA:", response.choices[0].message.content.strip())
