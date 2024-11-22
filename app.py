import streamlit as st
from src.components import models_table, prompt_input, raw_request, raw_response
from src.services.bedrock_service import list_fundation_models_api

def main():
    st.set_page_config(page_title="Bedrock Developer Assistant", layout="wide")
    st.title("Bedrock Developer Assistant")
    st.caption("A developer tool for prompt engineering and interacting with AWS Bedrock.")

    models = list_fundation_models_api()
    st.write(models)
    # Layout for models, prompt, raw request, and raw response
    with st.container():
        col1, col2 = st.columns([2, 1])
        with col1:
            selected_model_ids = models_table.display(models)
        with col2:
            prompt = prompt_input.get_prompt_input()

    col3, col4 = st.columns(2)
    with col3:
        raw_requests = raw_request.get_raw_request(selected_model_ids, prompt)
    with col4:
        raw_response.display_responses(raw_requests)

if __name__ == "__main__":
    main()

