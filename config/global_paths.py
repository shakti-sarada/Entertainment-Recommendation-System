import os

# Base project directory
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Data directories
DATA_DIR = os.path.join(BASE_DIR, 'data')
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, 'processed_data')
ARTIFACT_DIR = os.path.join(BASE_DIR, 'artifacts')

# Domain subdirectories
DOMAINS = ['anime', 'movie', 'web_series']
PROCESSED_PATHS = {d: os.path.join(PROCESSED_DATA_DIR, d, f"{d}.csv") for d in DOMAINS}
ARTIFACT_PATHS = {d: os.path.join(ARTIFACT_DIR, d) for d in DOMAINS}

# Accessor functions
def get_processed_csv_path(domain):
    return PROCESSED_PATHS[domain]

def get_artifact_path(domain, filename):
    return os.path.join(ARTIFACT_PATHS[domain], filename)