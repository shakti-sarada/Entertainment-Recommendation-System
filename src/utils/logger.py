import logging
import os

# Create logs directory if not exists
os.makedirs("logs", exist_ok=True)

# Set up logger
logger = logging.getLogger("recommender_logger")
logger.setLevel(logging.INFO)

# File handler
file_handler = logging.FileHandler("logs/system.log")
file_handler.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Add handler to logger
if not logger.hasHandlers():
    logger.addHandler(file_handler)
