from fastapi import FastAPI
from pydantic import BaseModel
from fraud_detection.models.predict import FraudPredictor

app = FastAPI(
    title="Fraud Detection Microservice",
    description="Microservice pour la détection de fraude fiscale",
    version="1.0.0"
)

predictor = FraudPredictor()

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