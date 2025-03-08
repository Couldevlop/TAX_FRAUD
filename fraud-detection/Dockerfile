FROM python:3.12-slim

WORKDIR /app

# Installation des dépendances système nécessaires
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Mise à jour de pip
RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt --verbose

# Copie des répertoires et fichiers
COPY ./models /app/models
COPY ./api /app/api

CMD ["uvicorn", "api.fraud_api:app", "--host", "0.0.0.0", "--port", "8001"]