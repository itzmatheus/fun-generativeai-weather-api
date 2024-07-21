import os
from pathlib import Path
from starlette.config import Config


BASE_DIR = Path(__file__).resolve().parent.parent.parent
env_path = os.path.join(BASE_DIR, ".env")
config = Config(env_path)

OPEN_AI_KEY = os.getenv("OPENAI_API_KEY") or config("OPENAI_API_KEY")
