class ModelNativeRequest:
    def __init__(self, model_id, prompt):
        self.model_id = model_id
        self.prompt = prompt
        self.models_config = {
            "anthropic.claude-3-5-sonnet-20240620-v1:0": {
                "max_tokens": 512,
                "temperature": 0.5,
                "anthropic_version": "bedrock-2023-05-31",
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": None
                            },
                        ],
                    }
                ]
            },
            "anthropic.claude-3-haiku-20240307-v1:0": {
                "max_tokens": 512,
                "temperature": 0.5,
                "anthropic_version": "bedrock-2023-05-31",
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": None
                            },
                        ],
                    }
                ]
            },
            "anthropic.claude-v2": {
                "prompt": None,
                "max_tokens_to_sample": 300,
                "temperature": 0.1,
                "top_p": 0.9,
            }
        }


    def get_request(self):
        """
        Fetches the native request configuration for the specified model ID.

        Args:
            model_id (str): The model ID for which to fetch the request configuration.

        Returns:
            dict: The request configuration with the dynamic prompt inserted, or an empty dict if not found.
        """
        config = self.models_config.get(self.model_id)
        if not config:
            return {}

        # Deep copy to avoid mutating the original configuration
        request_config = {**config}
        if "prompt" in request_config:
            request_config["prompt"] = self.prompt
        if "messages" in request_config:
            for message in request_config["messages"]:
                for content in message.get("content", []):
                    if "text" in content:
                        content["text"] = self.prompt

        return request_config