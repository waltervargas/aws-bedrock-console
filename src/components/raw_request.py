import streamlit as st
import json
from src.core.model_requests import ModelNativeRequest
from streamlit_ace import st_ace

def get_raw_request(selected_model_ids, prompt):
    """
    Dynamically generates raw requests for selected models and stores them in session state.
    """
    st.subheader("Raw Request")
    st.write("The raw JSON request automatically populates below based on your inputs.")

    if not selected_model_ids or not prompt:
        st.warning("Select models and enter a prompt to generate a raw request.")
        return

    # Initialize session state for raw requests if not already present
    if "raw_requests" not in st.session_state:
        st.session_state["raw_requests"] = {}

    # Update raw_requests in session state based on selected_model_ids
    for model_id in selected_model_ids:
        if model_id not in st.session_state["raw_requests"]:
            # Generate the raw request only if it doesn't already exist
            raw_request = ModelNativeRequest(model_id, prompt).get_request()
            st.session_state["raw_requests"][model_id] = raw_request

    # Remove requests for unselected models
    for model_id in list(st.session_state["raw_requests"].keys()):
        if model_id not in selected_model_ids:
            del st.session_state["raw_requests"][model_id]

    # Display all raw requests using unique keys
    for idx, (model_id, raw_request) in enumerate(st.session_state["raw_requests"].items()):
        st.write(f"Request for Model ID: {model_id}")
        st_ace(
            value=json.dumps(raw_request, indent=4),
            language="json",
            key=f"st_ace_{idx}"  # Unique key for each editor
        )

