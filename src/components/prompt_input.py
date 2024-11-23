import streamlit as st

def get_prompt_input():
    prompt = st.text_area("Enter your prompt >", placeholder="<Enter your prompt here>")
    return prompt
