import streamlit as st

def get_prompt_input():
    st.subheader("Prompt")
    st.write("Enter your prompt in the multiline text input below.")
    prompt = st.text_area("Multiline Text", placeholder="<Enter your prompt here>")
    return prompt
