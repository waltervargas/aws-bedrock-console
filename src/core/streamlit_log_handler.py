from io import StringIO
import logging

class StreamlitLogHandler(logging.Handler):
    """
    Custom logging handler to capture logs for Streamlit display.
    """
    def __init__(self):
        super().__init__()
        self.log_buffer = StringIO()

    def emit(self, record):
        log_entry = self.format(record)
        self.log_buffer.write(log_entry + "\n")

    def get_logs(self):
        """
        Returns the captured logs as a string and clears the buffer.
        """
        logs = self.log_buffer.getvalue()
        self.log_buffer.truncate(0)
        self.log_buffer.seek(0)
        return logs
