import streamlit as st
import json
from src.core.model_requests import ModelNativeRequest
from streamlit_ace import st_ace

def get_raw_request(selected_model_ids, prompt):
    """
    Dynamically generates and allows editing of raw requests for selected models.
    Tracks user edits in session state.
    """
    st.subheader("Raw Request")
    st.write("The raw JSON request automatically populates below based on your inputs.")

    if not selected_model_ids or not prompt:
        st.warning("Select models and enter a prompt to generate a raw request.")
        return None

    # Initialize session state for raw requests if not already present
    if "raw_requests" not in st.session_state:
        st.session_state["raw_requests"] = {}

    # Generate or retrieve raw requests for each selected model
    for idx, model_id in enumerate(selected_model_ids):
        # Generate a default request if not already present in session state
        if model_id not in st.session_state["raw_requests"]:
            default_request = ModelNativeRequest(model_id, prompt).get_request()
            st.session_state["raw_requests"][model_id] = default_request

        # Render the code editor for the current request
        st.write(f"Request for Model ID: {model_id}")
        edited_request = st_ace(
            value=json.dumps(st.session_state["raw_requests"][model_id], indent=4),
            language="json",
            key=f"st_ace_{model_id}",  # Unique key for each editor
            height=300,
        )

        # Update session state with the edited request if not None
        if edited_request:
            try:
                st.session_state["raw_requests"][model_id] = json.loads(edited_request)
            except json.JSONDecodeError:
                st.error(f"Invalid JSON in the request for Model ID: {model_id}")

    return st.session_state["raw_requests"]


