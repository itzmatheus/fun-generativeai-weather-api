import os
from pathlib import Path
from starlette.config import Config


BASE_DIR = Path(__file__).resolve().parent.parent.parent
env_path = os.path.join(BASE_DIR, ".env")
config = Config(env_path)

OPEN_AI_KEY        = os.getenv("OPENAI_API_KEY") or config("OPENAI_API_KEY") or None

LM_STUDIO_API_KEY  = os.getenv("LM_STUDIO_API_KEY") or config("LM_STUDIO_API_KEY") or None
LM_STUDIO_BASE_URL = os.getenv("LM_STUDIO_BASE_URL") or config("LM_STUDIO_BASE_URL") or None
LM_STUDIO_MODEL    = os.getenv("LM_STUDIO_MODEL") or config("LM_STUDIO_MODEL")  or None

USE_EXTERNAL_GEN_AI: bool = True

if LM_STUDIO_API_KEY and LM_STUDIO_BASE_URL and LM_STUDIO_MODEL:
    USE_EXTERNAL_GEN_AI = False