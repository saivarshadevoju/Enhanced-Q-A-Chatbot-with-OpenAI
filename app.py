import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import openai
import os
import dotenv
dotenv.load_dotenv()

# Langsmith Tracking 
langchain_api_key = os.getenv('LANGCHAIN_API_KEY')
langchain_project = os.getenv('LANGCHAIN_PROJECT')

if langchain_api_key:
    os.environ['LANGCHAIN_API_KEY'] = langchain_api_key

if langchain_project:
    os.environ['LANGCHAIN_PROJECT'] = langchain_project

# Keep tracing off unless you explicitly enable it in your environment.
if os.getenv('LANGCHAIN_TRACING_V2', '').lower() == 'true' and langchain_api_key:
    os.environ['LANGCHAIN_TRACING_V2'] = 'true'

# Prompt Template 

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please response to the user queries "),
        ("user","Question:{question}")
    ]
)

def generate_respose(question, api_key, model_name, temperature, max_token):
    openai.api_key = api_key
    llm = ChatOpenAI(
        model=model_name,
        temperature=temperature,
        max_tokens=max_token,
    )
    output_parser = StrOutputParser()
    chain = prompt|llm|output_parser
    answer = chain.invoke({'question':question })
    return answer 

# Title of the App
st.title("Enhanced Q&A Chatbot with OpenAI")

# Sidebar for settings
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter OpenAI API Key:",type="password")

# Dropdown to selsect various OpenAI model 
model_name = st.sidebar.selectbox("Select an OpenAI Model", ["gpt-5.5", "gpt-5.5-pro", "gpt-4.1"])

# Adjust response parameter
temperature = st.sidebar.slider("Temperature",min_value=0.0, max_value=1.0,value=0.7)
max_token = st.sidebar.slider("Max Tokens",min_value = 50, max_value=300, value=150)
user_input = st.text_input("Enter here")

if user_input:
    response = generate_respose(user_input, api_key, model_name, temperature, max_token)
    st.write(response)
else:
    st.write("Please enter the query.")