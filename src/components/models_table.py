import streamlit as st
import pandas as pd

def display(models):
    df = pd.DataFrame(models)

    # Add metadata for search and display
    df["display_name"] = (
        df["modelName"]
        + " ("
        + df["providerName"]
        + ")"
        + " | Model ID: "
        + df["modelId"]
    )

    # Multiselect with enhanced display names
    selected_model_ids = st.multiselect(
        "Available Models",
        options=df["modelId"].tolist(),
        default=[],
        format_func=lambda model_id: df[df["modelId"] == model_id]["display_name"].values[0],
    )

    # Filtered DataFrame for selected models
    if selected_model_ids:
        filtered_df = df[df["modelId"].isin(selected_model_ids)]
    else:
        filtered_df = df

    # Display the full dataframe filtered by selection
    st.dataframe(filtered_df, use_container_width=True)

    return selected_model_ids
