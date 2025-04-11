
### src/cat/api/dependencies.py
from src.cat.core.net_ease.services import NetEaseService

def get_service() -> NetEaseService:
    return NetEaseService()