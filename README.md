# llama-data-analyst-agent
A command-line data analyst agent using LLaMA-4 Maverick via the Together API. Supports structured (CSV, Excel) and unstructured (PDF, TXT, DOCX, images) data, with interactive question-answering and visualization.

# LLaMA Data Analyst Agent

A command-line data analyst agent powered by LLaMA-4 Maverick (Together API).  
Supports structured (CSV, Excel) and unstructured (PDF, TXT, DOCX, images) data.  
Includes interactive Q&A and data visualization.

## Features

- Loads and previews structured data (.csv, .xlsx)
- Extracts text from unstructured files (.pdf, .txt, .docx, .jpg, .png)
- Uses LLaMA-4 Maverick for question-answering about your data or documents
- Visualizes numeric data (scatter plots, histograms)
- Simple command-line interface

## Files

- `assignment.py` — Main CLI agent using LLaMA-4 Maverick
- `SN-project.py` — Alternate implementation of the agent
- `test.py` — Minimal test for LLaMA API integration
- `test.txt` — Example input file for testing
