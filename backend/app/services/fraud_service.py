import httpx
from sqlalchemy.orm import Session
from app.models.tax import Declaration
from app.repositories.tax_repository import TaxRepository

class FraudService:
    def __init__(self, db: Session):
        self.repository = TaxRepository(db)
        self.fraud_api_url = "http://fraud-detection:8001/predict"

    async def detect_fraud(self, declaration: Declaration) -> dict:
        # Préparation des données pour le microservice
        data Living = {
            "amount": declaration.amount,
            "fiscal_year": declaration.fiscal_year
        }

        # Appel au microservice fraud-detection
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(self.fraud_api_url, json=data)
                response.raise_for_status()
                prediction = response.json()
            except httpx.RequestError as e:
                prediction = {
                    "iso_forest_score": 0.5,
                    "xgboost_score": 0.5,
                    "neural_net_score": 0.5,
                    "ensemble_score": 0.5,
                    "is_fraudulent": False,
                    "error": str(e)
                }

        # Sauvegarde de la prédiction
        prediction_db = {
            "declaration_id": declaration.id,
            **prediction
        }
        self.repository.create_fraud_prediction(prediction_db)

        # Mise à jour du statut et audit
        if prediction.get("is_fraudulent", False):
            self.repository.update_declaration_status(declaration.id, "flagged")
            self.repository.create_audit_log(
                user_id=None,
                declaration_id=declaration.id,
                action="flagged",
                details={"reason": "Potential fraud detected", "score": prediction["ensemble_score"]}
            )

        return prediction