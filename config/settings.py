"""
=========================================================
Application Settings
=========================================================
"""

import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# =========================================================
# Application Information
# =========================================================

APP_NAME = "Personal AI Productivity & Automation Agent"

APP_VERSION = "1.0.0"

APP_DESCRIPTION = (
    "AI Assistant for Email, Meetings, Planning, "
    "Content Creation and Productivity"
)

# =========================================================
# Groq API
# =========================================================

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# =========================================================
# Upload Settings
# =========================================================

UPLOAD_FOLDER = "uploads"

SUPPORTED_FILE_TYPES = [
    "pdf",
    "txt"
]

MAX_FILE_SIZE_MB = 10

# =========================================================
# Chat Settings
# =========================================================

MAX_CHAT_HISTORY = 10

# =========================================================
# Logging
# =========================================================

LOG_LEVEL = "INFO"

# =========================================================
# Theme
# =========================================================

DEFAULT_THEME = "Light"

# =========================================================
# Download Folder
# =========================================================

DOWNLOAD_FOLDER = "downloads"


