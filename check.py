# Agent_ai_candidate/check_env.py
import os
from dotenv import load_dotenv

# Absolute path to your .env file (copy-paste your actual one)
ENV_PATH = r"C:\Users\User\Desktop\QBS\Xource(zehra_work)\Agent_ai_candidate\.env"

print(f"Looking for .env at: {ENV_PATH}")

# Load it explicitly
loaded = load_dotenv(dotenv_path=ENV_PATH)

print("Loaded:", loaded)
print("Current working directory:", os.getcwd())
print("Key value:", os.getenv("GROQ_API_KEY"))
