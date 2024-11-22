import json
import boto3

def invoke_model_api(model_id, request):
    # Initialize Bedrock client
    client = boto3.client("bedrock-runtime", region_name="eu-central-1")  # Update region as needed

    try:
        response = client.invoke_model(
            modelId=model_id,
            body=json.dumps(request),
        )

        # Parse and return the response
        return json.loads(response["body"].read().decode("utf-8"))
    except Exception as e:
        return {"error": str(e)}
    
def list_fundation_models_api():
    client = boto3.client("bedrock", region_name="eu-central-1")
    try:
        response = client.list_foundation_models()
        return response.get("modelSummaries", [])
    except Exception as e:
        return {"error": str(e)}
