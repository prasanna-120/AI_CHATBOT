# 🤖 LangChain + Ollama + Streamlit Chatbot

A modern AI chatbot built using **LangChain**, **Ollama**, and **Streamlit**. This application runs **locally** on your computer using an Ollama language model, so no OpenAI API key is required.

---

# 🚀 Features

* 🧠 Runs local LLMs using Ollama
* 💬 Interactive chat interface with Streamlit
* 🔗 Prompt management using LangChain
* ⚡ Fast local inference
* 🔒 Privacy-friendly (no cloud API required)
* 📜 Chat history during the session
* 🎯 Beginner-friendly project structure

---

# 🛠️ Tech Stack

* Python 3.11+
* Streamlit
* LangChain
* LangChain Ollama
* Ollama

---

# 📂 Project Structure

```text
LangChain-Ollama-Chatbot/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── venv/
```

---

# 📦 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/LangChain-Ollama-Chatbot.git
```

```bash
cd LangChain-Ollama-Chatbot
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Install Ollama

Download and install Ollama from:

https://ollama.com/download

Verify installation:

```bash
ollama --version
```

---

# Download the LLM Model

Example using Llama 3.1:

```bash
ollama pull llama3.1
```

Check installed models:

```bash
ollama list
```

---

# Start the Ollama Server

```bash
ollama serve
```

If the server is already running, you can skip this step.

---

# Run the Streamlit Application

```bash
streamlit run app.py
```

Open your browser and visit:

```
http://localhost:8501
```

---

# Example Questions

* What is Artificial Intelligence?
* Explain Machine Learning.
* What is LangChain?
* Write a Python program to reverse a string.
* Explain Neural Networks in simple words.

---

# Requirements

```
streamlit
langchain
langchain-core
langchain-ollama
```

---

# Application Workflow

```
User
   │
   ▼
Streamlit Interface
   │
   ▼
ChatPromptTemplate
   │
   ▼
OllamaLLM
   │
   ▼
StrOutputParser
   │
   ▼
AI Response
```

---

# Advantages

* No OpenAI API key required
* Runs completely on your local machine
* Easy to customize prompts
* Beginner-friendly
* Supports multiple Ollama models
* Works offline after the model has been downloaded

---

# Future Enhancements

* Conversation memory
* Streaming responses
* PDF Question Answering (RAG)
* Website Chatbot
* YouTube Video Chat
* SQL Database Chatbot
* Voice Assistant
* Multi-model support
* Dark mode UI
* Docker deployment

---

# License

This project is released under the MIT License.

---

# Author

**PRASANNA**

* Aspiring Data Scientist
* Full Stack Developer
* Generative AI Enthusiast

If you found this project helpful, consider giving it a ⭐ on GitHub.
