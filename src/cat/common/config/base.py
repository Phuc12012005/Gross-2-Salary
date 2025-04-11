
### src/cat/common/config/base.py
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "CAT App")

settings = Settings()
