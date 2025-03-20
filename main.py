#pip install python-dotenv
#pip install langchain-openai
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
from langchain_openai import ChatOpenAI
chat_model = ChatOpenAI(api_key=api_key)

result = chat_model.invoke("AI에 대한 시를 써줘.")
print(result.content)
st.write(result.content)

