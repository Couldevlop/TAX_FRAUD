from fastapi import FastAPI
from pydantic import BaseModel
from models.predict import FraudPredictor
from models.train_model import train_models
import pandas as pd
import numpy as np
import os

app = FastAPI(
    title="Fraud Detection Microservice",
    description="Microservice pour la détection de fraude fiscale",
    version="1.0.0"
)

# Initialisation du prédicteur
model_path = "/app/models/"
if not all(os.path.exists(f"{model_path}{model}.pkl") for model in ["scaler", "iso_forest", "xgboost", "neural_net"]):
    # Données simulées pour l'entraînement
    data = pd.DataFrame({
        'amount': np.random.uniform(10000, 1000000, 1000),
        'fiscal_year': np.random.randint(2020, 2024, 1000)
    })
    train_models(data, save_path=model_path)

predictor = FraudPredictor(model_path=model_path)

class DeclarationInput(BaseModel):
    amount: float
    fiscal_year: int

@app.post("/predict", response_model=dict)
async def predict_fraud(data: DeclarationInput):
    prediction = predictor.predict(data.dict())
    return prediction

@app.get("/health")
async def health_check():
    return {"status": "healthy"}