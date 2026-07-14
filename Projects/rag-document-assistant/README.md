# RAG Document Assistant

## Project Overview

RAG Document Assistant is a Retrieval-Augmented Generation (RAG) application built using Python, ChromaDB, Sentence Transformers, and the OpenRouter API. The application allows users to upload one or more PDF documents, ask questions, and receive answers generated only from the uploaded documents.

---

## Features

- Load multiple PDF documents
- Split documents into text chunks
- Generate embeddings using Sentence Transformers
- Store embeddings in ChromaDB
- Retrieve the most relevant document chunks
- Generate answers using the OpenRouter API
- Display source document name
- Display source page number
- Simple Streamlit web interface
- Multiple document support
- Graceful error handling
- Reduces hallucinations by using document context

---

## Technologies Used

- Python 3.14
- ChromaDB
- Sentence Transformers
- OpenRouter API
- PyPDF
- Streamlit
- python-dotenv

---

## Project Structure

```
rag-document-assistant/
│
├── app.py
├── streamlit_app.py
├── config.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore
├── data/
├── vector_db/
├── utils/
│   ├── document_loader.py
│   ├── vector_store.py
│   ├── rag_pipeline.py
│   └── llm.py
└── screenshots/
```

---

## Installation

### 1. Clone the repository

```bash
git clone <repository_url>
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file

```text
OPENROUTER_API_KEY=your_api_key_here
```

### 4. Run the Console Application

```bash
python app.py
```

### 5. Run the Streamlit Web Application

```bash
streamlit run streamlit_app.py
```

or

```bash
python -m streamlit run streamlit_app.py
```

---

## Sample Output

**Question**

```
What is Python?
```

**Answer**

```
Python is a high-level, interpreted programming language created by Guido van Rossum. It is widely used in web development, AI, data science, and automation.
```

**Source**

```
Document: python_notes.pdf
Page: 2
```

---

## Purpose

This project demonstrates how Retrieval-Augmented Generation (RAG) improves AI accuracy by retrieving relevant information from uploaded PDF documents before generating answers. This reduces hallucinations and provides trustworthy, document-based responses.