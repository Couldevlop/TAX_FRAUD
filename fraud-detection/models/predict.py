import joblib
import pandas as pd
import numpy as np

class FraudPredictor:
    def __init__(self, model_path: str = "models/"):
        self.scaler = joblib.load(f"{model_path}scaler.pkl")
        self.iso_forest = joblib.load(f"{model_path}iso_forest.pkl")
        self.xgboost = joblib.load(f"{model_path}xgboost.pkl")
        self.neural_net = joblib.load(f"{model_path}neural_net.pkl")

    def predict(self, data: dict) -> dict:
        """
        Prédit les scores de fraude pour une déclaration donnée.
        """
        # Préparation des données
        df = pd.DataFrame([data])
        X = df[['amount', 'fiscal_year']]
        X_scaled = self.scaler.transform(X)

        # Prédictions
        iso_score = self.iso_forest.score_samples(X_scaled)[0] * -1  # Score positif
        xgb_score = self.xgboost.predict_proba(X_scaled)[0][1]  # Probabilité de fraude
        nn_score = self.neural_net.predict_proba(X_scaled)[0][1]  # Probabilité de fraude
        
        # Score d'ensemble (moyenne pondérée)
        ensemble_score = (iso_score + xgb_score + nn_score) / 3
        is_fraudulent = ensemble_score > 0.7

        return {
            "iso_forest_score": float(iso_score),
            "xgboost_score": float(xgb_score),
            "neural_net_score": float(nn_score),
            "ensemble_score": float(ensemble_score),
            "is_fraudulent": is_fraudulent
        }