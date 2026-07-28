# Loads important/reusable info
import os
from pathlib import Path

from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parent
load_dotenv(PROJECT_ROOT / ".env")

DEFAULT_CITY = os.getenv("DEFAULT_CITY", "Dallas")
TIMEZONE = os.getenv("TIMEZONE", "America/Chicago")