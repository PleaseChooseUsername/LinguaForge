import streamlit as st
from langchain.llms import openai

st.title('Test app')
open_api_key = st.sidebar.text_input('OpenAI API Key')

def generate_response(input_text):
    llm = OpenAI(temperature=0.7, open_api_key=open_api_key)
    st.info(llm(input_text))

with st.form('my_form'):
    text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    submitted = st.form_submit_button('Submit')
    if not open_api_key.startswith('-sk'):
       st.warning('Please enter valid OpenAI API key', icon='⚠')
    if submitted and open_api_key.startswith('sk-'):
       generate_response(text)"
