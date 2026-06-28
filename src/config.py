"""
Configuration file for AI Network Intrusion Detection System
"""

from pathlib import Path

# ==============================
# Project Directories
# ==============================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
MODEL_DIR = BASE_DIR / "models"
LOG_DIR = BASE_DIR / "logs"

# ==============================
# Dataset & Model
# ==============================

DATASET_FILE = DATA_DIR / "cicids.csv"
MODEL_FILE = MODEL_DIR / "nids_model.pkl"

# ==============================
# Flow Settings
# ==============================

FLOW_TIMEOUT = 30      # seconds
MAX_PACKETS = 20

# ==============================
# Dashboard
# ==============================

REFRESH_RATE = 2

# ==============================
# Logging
# ==============================

LOG_FILE = LOG_DIR / "alerts.csv"