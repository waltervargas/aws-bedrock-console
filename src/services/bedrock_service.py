import json
import boto3
import streamlit as st

def invoke_model_api(model_id, request):
    # Initialize Bedrock client
    client = boto3.client("bedrock-runtime", region_name="eu-central-1")  # Update region as needed

    print(f"Invoking model {model_id} with request: {request}\n")
    try:
        response = client.invoke_model(
            modelId=model_id,
            body=json.dumps(request),
        )

        # Parse and return the response
        return json.loads(response["body"].read().decode("utf-8"))
    except Exception as e:
        return {"error": str(e)}
    
import boto3
from botocore.exceptions import ClientError

st.cache_data
def list_fundation_models_api(region):
    """
    Fetches the foundation models from AWS Bedrock
    """
    client = boto3.client("bedrock", region_name=region)
    try:
        response = client.list_foundation_models()
        return response.get("modelSummaries", [])
    except ClientError as e:
        if e.response["Error"]["Code"] == "ExpiredToken":
            return {"error": "Your AWS credentials have expired. Please refresh your credentials and try again."}
        else:
            return {"error": f"An error occurred: {e.response['Error']['Message']}"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {str(e)}"}

