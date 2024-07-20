import os
from pathlib import Path
from starlette.config import Config

from openai import OpenAI

BASE_DIR = Path(__file__).resolve().parent.parent.parent
env_path = os.path.join(BASE_DIR, ".env")
config = Config(env_path)

OPEN_AI_KEY = config("OPENAI_API_KEY")
open_ai_client = OpenAI(api_key=OPEN_AI_KEY)