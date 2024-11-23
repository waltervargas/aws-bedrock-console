import streamlit as st
import logging

def display_boto3_logs(log_handler):
    """
    Displays Boto3 logs captured in the custom log handler with filtering and search.
    """
    with st.expander("Boto3 API Logs", expanded=True):
        logs = log_handler.get_logs()

        if logs:
            # Add search functionality
            search_query = st.text_input("Search Logs")
            if search_query:
                logs = "\n".join([line for line in logs.split("\n") if search_query in line])

            st.code(logs, language="json")
        else:
            st.info("No logs to display yet.")