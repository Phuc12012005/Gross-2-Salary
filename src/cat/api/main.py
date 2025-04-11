### src/cat/api/main.py
from fastapi import FastAPI
from src.cat.api.routers import net_ease

app = FastAPI(title="CAT API")

app.include_router(net_ease.router, prefix="/net-ease", tags=["Net Ease"])