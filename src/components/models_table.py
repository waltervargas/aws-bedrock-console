import streamlit as st

def display(models):
    st.subheader("Models")
    st.write("Select one or more models from the list below:")

    if "error" in models[0]:
        st.error(f"Error fetching models: {models[0]['error']}")
        return []

    try:
        # Map modelId to modelName
        model_mapping = {model["modelId"]: model["modelName"] for model in models}
    except KeyError as e:
        st.error(f"Invalid data structure: Missing key {e}")
        return []

    # Multiselect with modelId as the stored value
    selected_model_ids = st.multiselect(
        "Available Models",
        options=model_mapping.keys(),
        format_func=lambda model_id: f"{model_mapping[model_id]}"
    )

    st.write("Selected Models (IDs):", selected_model_ids)
    return selected_model_ids
