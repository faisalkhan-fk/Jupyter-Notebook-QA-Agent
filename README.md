# 🤖 PDF Question Answering Agent

An AI-powered **PDF Question Answering Agent** built using Python and Jupyter Notebook. The agent reads and processes the content of a PDF document and answers user questions based on the information available in that document.

Instead of manually searching through a long PDF, users can simply ask questions and get relevant answers from the document.

---

## 🚀 Features

* 📄 Reads and processes PDF documents
* 🔍 Extracts text from PDF files
* ✂️ Splits extracted content into smaller chunks
* 🧠 Generates embeddings for document content
* 🔎 Retrieves relevant information based on the user's question
* 🤖 Uses Generative AI to generate answers
* 💬 Answers questions based on the uploaded PDF
* 📚 Useful for study material, reports, notes, policies, and documentation

---

## 🛠️ Technologies Used

* **Python**
* **Jupyter Notebook**
* **Google Gemini AI**
* **PyMuPDF**
* **Sentence Transformers**
* **FAISS**
* **NumPy**
* **python-dotenv**

---

## 🔄 How It Works

The agent follows a Retrieval-Augmented Generation (RAG) based approach:

```text
              📄 PDF Document
                    ↓
              Extract Text
                    ↓
              Create Chunks
                    ↓
          Generate Embeddings
                    ↓
              FAISS Index
                    ↓
             User Question
                    ↓
        Find Relevant Information
                    ↓
             Gemini AI Model
                    ↓
              💬 Final Answer
```

### Step-by-Step

1. The user provides a PDF document.
2. The system extracts text from the PDF using **PyMuPDF**.
3. The extracted text is divided into smaller chunks.
4. **Sentence Transformers** converts the chunks into numerical embeddings.
5. The embeddings are stored in a **FAISS** vector index.
6. When the user asks a question, the system searches for the most relevant chunks.
7. The relevant context is provided to the **Gemini AI model**.
8. Gemini generates an answer based on the retrieved PDF content.

---

## 📂 Project Structure

```text
PDF-Question-Answering-Agent/
│
├── QA Agent.ipynb
├── README.md
└── .env
```

> ⚠️ Never upload your actual API key to GitHub. Store it inside `.env` and add `.env` to `.gitignore`.

---

## 📦 Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Move into the project directory:

```bash
cd PDF-Question-Answering-Agent
```

Install the required libraries:

```bash
pip install google-generativeai python-dotenv pymupdf sentence-transformers faiss-cpu numpy
```

Install Jupyter Notebook if required:

```bash
pip install notebook
```

---

## 🔑 API Key Configuration

Create a `.env` file in the project directory:

```env
GEMINI_API_KEY=your_api_key_here
```

Then load the API key in Python:

```python
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
```

Make sure `.env` is included in `.gitignore`:

```text
.env
```

---

## ▶️ How to Run

Start Jupyter Notebook:

```bash
jupyter notebook
```

Then open:

```text
QA Agent.ipynb
```

Run the notebook cells sequentially.

Upload/provide your PDF document and ask questions related to its content.

---

## 💡 Example

### Input PDF

```text
Placement Policy 2027.pdf
```

### User Question

```text
What are the eligibility criteria mentioned in the placement policy?
```

### Agent

The system retrieves the relevant information from the PDF and generates an answer using the retrieved context.

---

## 🎯 Use Cases

This project can be used for:

* 📚 Academic notes
* 🎓 College placement policies
* 📄 Research papers
* 📖 Study materials
* 🏢 Company documentation
* 📋 Policies and guidelines
* 📑 Reports
* 📘 Technical documentation

---

## 🔮 Future Improvements

* 🌐 Convert the notebook into a web application
* 💬 Add a chat-based interface
* 📂 Support multiple PDF documents
* 💾 Store conversation history
* ⚡ Improve retrieval accuracy
* 📊 Add document analytics
* 🔐 Add secure authentication
* ☁️ Deploy the application online

---

## 👨‍💻 Author

**Faisal Khan**

MCA Student | AI & Full Stack Developer

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.
