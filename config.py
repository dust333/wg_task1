import os

from dotenv import load_dotenv

ROOT_PATH = f"{os.path.dirname(os.path.abspath(__file__))}/"

if os.path.exists(env_file := ROOT_PATH + ".env"):
    load_dotenv(env_file)

LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG")
WIKI_URL = os.getenv("WIKI_URL", "")
