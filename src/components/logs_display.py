import streamlit as st
import logging
import json

def display_boto3_logs(log_handler):
    """
    Displays Boto3 logs captured in the custom log handler with a filter for log source names.
    """
    with st.expander("Boto3 API Logs (Filtered by Name)", expanded=True):
        # Fetch logs from the handler
        logs = log_handler.get_logs()
        
        if logs:
            # Parse the logs into JSON objects
            log_entries = [json.loads(log) for log in logs.splitlines()]
            
            # Extract unique log names
            log_names = sorted({entry["name"] for entry in log_entries})
            log_names.insert(0, "all")  # Add "all" as the default option

            # Add a multi-select box for log filtering
            selected_names = st.multiselect(
                "Filter by Log Source",
                options=log_names,
                default=["botocore.endpoint"]
            )

            # Filter logs based on selected names
            if "all" not in selected_names:
                filtered_logs = [
                    entry for entry in log_entries if entry["name"] in selected_names
                ]
            else:
                filtered_logs = log_entries  # Show all logs if "all" is selected

            # Display the filtered logs in JSON format
            if filtered_logs:
                st.code(json.dumps(filtered_logs, indent=2), language="json")
            else:
                st.info("No logs match the selected filters.")
        else:
            st.info("No logs to display yet.")