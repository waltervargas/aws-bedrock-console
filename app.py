import streamlit as st
from src.components import (
    models_table, 
    prompt_input, 
    raw_request, 
    raw_response, 
    region_selector,
    logs_display,
)
from src.services.bedrock_service import list_fundation_models_api
from src.core.logger import configure_boto3_logger
from src.core.streamlit_log_handler import StreamlitLogHandler
import logging

def main():
    st.set_page_config(page_title="Bedrock Developer Assistant", layout="wide")

    if "log_handler" not in st.session_state:
        st.session_state["log_handler"] = StreamlitLogHandler()  # Initialize the log handler

    log_handler = st.session_state["log_handler"]
    configure_boto3_logger(level=logging.DEBUG)
    logging.getLogger("botocore").addHandler(log_handler)
    logging.getLogger("boto3").addHandler(log_handler)

    selected_region = region_selector.select_region()

    models_response = list_fundation_models_api(region=selected_region)
    if isinstance(models_response, dict) and "error" in models_response:
        st.error(models_response["error"])
        st.info("Please ensure your AWS credentials are refreshed before retrying.")
        return
    models = models_response
    
    if "prompt" not in st.session_state:
        st.session_state["prompt"] = ""
    if "selected_model_ids" not in st.session_state:
        st.session_state["selected_model_ids"] = []

    st.session_state["prompt"] = prompt_input.get_prompt_input()
    st.session_state["selected_model_ids"] = models_table.display(models)

    col1, col2 = st.columns(2)
    with col1:
        raw_request.get_raw_request(
            st.session_state["selected_model_ids"], 
            st.session_state["prompt"]
        )
    with col2:
        raw_response.display_responses(st.session_state.get("raw_requests", {}))

     # Display captured logs
    logs_display.display_boto3_logs(log_handler)

if __name__ == "__main__":
    main()

