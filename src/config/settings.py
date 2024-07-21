import os
from pathlib import Path
from starlette.config import Config


BASE_DIR = Path(__file__).resolve().parent.parent.parent
env_path = os.path.join(BASE_DIR, ".env.test")
config = Config(env_path)

OPEN_AI_KEY = config("OPENAI_API_KEY")
