import os
from dotenv import load_dotenv
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA_DIR = ROOT / "data"

JOBS_PATH = DATA_DIR / "linkedin_jobs_500.json"
EMBEDDINGS_PATH = DATA_DIR / "embeddings.npy"

MODEL_EMB_NAME = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"



load_dotenv(ROOT / ".env")
ANTHROPIC_API_KEY = os.environ["ANTHROPIC_API_KEY"]
MODEL_ANTHROPIC = "claude-haiku-4-5-20251001"