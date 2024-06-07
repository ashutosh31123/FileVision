import streamlit as st
from dotenv import load_dotenv
from utils import query_agent

load_dotenv()

st.title("Let's analyze your file")
st.header("Please upload your CSV file here")

data=st.file_uploader("Upload CSV file",type="csv")

query=st.text_area("Enter your query")
button=st.button("Submit")

if button:
    answer=query_agent(data,query)
    st.write(answer)