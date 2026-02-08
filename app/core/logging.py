import logging

"""
logging setup for the application.
"""

def setup_logging():
    logging.basicConfig(
        level = logging.INFO,
        format = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )