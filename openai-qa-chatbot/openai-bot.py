import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os

from dotenv import load_dotenv
load_dotenv()

# Load environment variables
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]="Simple Q&A Chatbot With OPENAI"

# Chat prompt template
prompt =  ChatPromptTemplate.from_messages(
    [
        ("system", "You are a Helpful assistant, please answer the user questions"),
        ("user", "Question: {question}")
    ]
)

# Create the function to gerate the response
def generate_response(question, api_key, model):
    # Create the chatbot
    openai.api_key = api_key

    llm = ChatOpenAI(model=model)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser # Create the chain

    answer = chain.invoke({"question": question}) # Invoke the chain

    return answer

st.title("Q&A Chatbot using OpenAI")


# Create a sidebar for the settings
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")
model = st.sidebar.selectbox("Select OpenAI Model", ["gpt-3.5-turbo", "gpt-4o", "gpt-4o-turbo", "gpt-4"])

st.write("This is a simple Q&A chatbot using OpenAI. Please enter your question below")
question = st.text_input("Enter your question")

if st.button("Get Answer"):
    if api_key:
        answer = generate_response(question, api_key, "gpt-3.5-turbo")
        st.write(answer)
    else:
        st.write("Please enter your OpenAI API Key in the settings")
