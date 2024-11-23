import streamlit as st

def display_boto3_logs(log_handler):
    """
    Displays Boto3 logs captured in the custom log handler.
    """
    logs = log_handler.get_logs()
    if logs:
        st.text_area("Boto3 Logs", logs, height=300)
    else:
        st.info("No logs to display yet.")