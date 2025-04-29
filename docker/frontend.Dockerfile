FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY packages/ packages/

EXPOSE 8501

CMD ["bash", "-c", "PYTHONPATH=packages/dev_ui/src streamlit run packages/dev_ui/src/dev_ui/ui/pages/Homepage.py --server.address 0.0.0.0 --server.port 8501"]
