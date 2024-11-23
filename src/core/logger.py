import boto3
import logging

def configure_boto3_logger():
    """
    Configures the boto3 and botocore logger to verbose mode using set_stream_logger.
    """
    # Set the Boto3 logger to DEBUG level
    boto3.set_stream_logger(name="boto3", level=logging.DEBUG)

    # Set the Botocore logger to DEBUG level for detailed HTTP wire traces
    boto3.set_stream_logger(name="botocore", level=logging.DEBUG)