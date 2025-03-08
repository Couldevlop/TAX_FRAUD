FROM python:3.12-slim

WORKDIR /app

# Installer les dépendances système nécessaires
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Mettre à jour pip
RUN pip install --upgrade pip

# Copier et installer les dépendances Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Installer pandas, psycopg2-binary et passlib
RUN pip install pandas psycopg2-binary passlib

# Créer un lien symbolique pour résoudre un éventuel problème de compatibilité
RUN ln -sf /usr/local/lib/python3.12/site-packages/jose /usr/local/lib/python3.12/site-packages/jwt

# Copier le script wait-for-db.sh et lui donner les permissions d'exécution
COPY wait-for-db.sh .
RUN chmod +x wait-for-db.sh

# Copier l'application et le script de génération de données
COPY ./app /app/app
COPY test_data_generator.py /app/

# Commande par défaut pour démarrer l'application
CMD ["./wait-for-db.sh", "db", "5432", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]