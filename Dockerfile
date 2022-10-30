FROM python:3.8-slim-buster as base

RUN apt update -y && apt install git -y
RUN pip install --no-cache-dir --upgrade fastapi uvicorn "dvc[s3]" joblib sklearn

COPY ./api.py api.py

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
