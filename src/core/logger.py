import boto3
import logging

import logging
import json

class JSONFormatter(logging.Formatter):
    """
    Custom formatter to output logs in JSON format.
    """
    def format(self, record):
        log_record = {
            "timestamp": self.formatTime(record, self.datefmt),
            "name": record.name,
            "level": record.levelname,
            "message": record.getMessage(),
        }
        # Include exception information if available
        if record.exc_info:
            log_record["exception"] = self.formatException(record.exc_info)
        return json.dumps(log_record)


def configure_boto3_logger(level=logging.DEBUG):
    """
    Configures the boto3 and botocore logger to output logs in JSON format.
    Args:
        level (int): Logging level (e.g., logging.DEBUG, logging.INFO).
    """
    # Define a JSON formatter
    json_formatter = JSONFormatter()

    # Set up the boto3 logger
    boto3_logger = logging.getLogger("boto3")
    boto3_logger.setLevel(level)
    boto3_handler = logging.StreamHandler()
    boto3_handler.setLevel(level)
    boto3_handler.setFormatter(json_formatter)
    boto3_logger.addHandler(boto3_handler)

    # Set up the botocore logger
    botocore_logger = logging.getLogger("botocore")
    botocore_logger.setLevel(level)
    botocore_handler = logging.StreamHandler()
    botocore_handler.setLevel(level)
    botocore_handler.setFormatter(json_formatter)
    botocore_logger.addHandler(botocore_handler)