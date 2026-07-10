import streamlit as st

from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# ---------------------------------
# Streamlit Configuration
# ---------------------------------

st.set_page_config(
    page_title="LangChain + Ollama",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Local AI Chatbot")
st.markdown("Powered by LangChain + Ollama")

# ---------------------------------
# Prompt Template
# ---------------------------------

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are an intelligent AI assistant.
            Give clear, simple and detailed answers.
            """
        ),
        ("human", "{question}")
    ]
)

# ---------------------------------
# Load LLM
# ---------------------------------

llm = OllamaLLM(
    model="llama3.2:3b",
    temperature=0.3
)

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

# ---------------------------------
# Chat History
# ---------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------------------------
# User Input
# ---------------------------------

question = st.chat_input("Ask me anything...")

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    answer = chain.invoke(
        {
            "question": question
        }
    )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    with st.chat_message("assistant"):
        st.markdown(answer)