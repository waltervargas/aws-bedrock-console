import streamlit as st
import json

def get_raw_request(selected_model_ids, prompt):
    st.subheader("Raw Request")
    st.write("The raw JSON request automatically populates below based on your inputs.")

    if not selected_model_ids or not prompt:
        st.warning("Select models and enter a prompt to generate a raw request.")
        return None

    raw_requests = {}

    # Generate a raw request JSON for each selected model
    for model_id in selected_model_ids:
        raw_request = {
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 512,
            "temperature": 0.5,
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text", 
                            "text": prompt
                        },
                    ],
                }
            ],
        }
        # Map the request to its corresponding model ID
        raw_requests[model_id] = raw_request

        # Display the request for this model in a code editor block
        st.write(f"Request for Model ID: {model_id}")
        st.code(json.dumps(raw_request, indent=4), language="json")

    return raw_requests
