FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ src/

EXPOSE 8000

CMD ["bash", "-c", "PYTHONPATH=src uvicorn cat.api.main:app --host 0.0.0.0 --port 8000 --reload"]
