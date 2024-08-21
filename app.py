# Q&A Chatbot
from langchain import HuggingFaceHub

import streamlit as st
import os

hugging_face_token = "Your token"

os.environ['HUGGINGFACEHUB_API_TOKEN'] = hugging_face_token
llm_huggingface=HuggingFaceHub(repo_id="google/flan-t5-large",model_kwargs={"temperature":0,"max_length":64})


def get_openai_response(question):

    response=llm_huggingface(question)
    return response

##initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Langchain Application")

input=st.text_input("Input: ",key="input")
response=get_openai_response(input)

submit=st.button("Ask the question")

## If ask button is clicked

if submit:
    st.subheader("The Response is")
    st.write(response)



