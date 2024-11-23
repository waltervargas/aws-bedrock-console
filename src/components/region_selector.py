import streamlit as st
from src.core.enums import AWSRegion


def select_region(default_region="eu-central-1"):
    """
    Displays a region selector at the top-right corner of the app and returns the selected region.
    """
    col1, col2 = st.columns([9, 1])  # Adjust column proportions to align the selector to the right

    with col2:
        selected_region = st.selectbox(
            "AWS Region",  # Label for the dropdown
            options=AWSRegion.list(),  # Use Enum's list method
            index=AWSRegion.list().index(default_region),  # Default index based on config
            label_visibility="collapsed",  # Hide the label for a cleaner look
        )
    return selected_region

