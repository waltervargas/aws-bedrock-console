import streamlit as st
import json
from src.services.bedrock_service import invoke_model_api

def display_responses(raw_requests):
    st.subheader("Raw Response")

    if not raw_requests:
        st.warning("Generate a raw request to see the response.")
        return

    # Add a button to trigger the API call
    if st.button("Call Bedrock InvokeModel API"):
        for model_id, request in raw_requests.items():
            # Send the request using the Bedrock API
            response = invoke_model_api(model_id, request)

            # Display the response dynamically
            st.write(f"Response for Model ID: {model_id}")
            st.code(json.dumps(response, indent=4), language="json")

