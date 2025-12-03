"""
Configuration settings for the Image Caption Generator application.
Automatically detects environment (local vs Hugging Face Spaces) and configures accordingly.
"""

import os

# Detect if running on Hugging Face Spaces
IS_HUGGINGFACE = os.getenv("SPACE_ID") is not None

# Gradio launch configuration
if IS_HUGGINGFACE:
    # Hugging Face Spaces configuration
    GRADIO_CONFIG = {
        "share": False,
        "show_error": True,
    }
    ENVIRONMENT = "huggingface"
else:
    # Local development configuration
    GRADIO_CONFIG = {
        "share": True,  # Creates a public URL (set to False for localhost only)
        "server_name": "127.0.0.1",
        "server_port": 7860,
        "show_error": True,
    }
    ENVIRONMENT = "local"

# Model configuration
MODEL_NAME = "Salesforce/blip-image-captioning-large"

# Caption generation settings
MAX_CAPTION_LENGTH = 50
NUM_BEAMS = 5

print(f"🔧 Configuration loaded: Running in {ENVIRONMENT} mode")
