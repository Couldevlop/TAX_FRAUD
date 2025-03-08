from sqlalchemy.orm import Session
from app.models.tax import Declaration, FraudPrediction, AuditLog
from datetime import datetime

class TaxRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_declaration_by_id(self, declaration_id: int):
        return self.db.query(Declaration).filter(Declaration.id == declaration_id).first()

    def create_fraud_prediction(self, prediction: dict):
        db_prediction = FraudPrediction(
            declaration_id=prediction["declaration_id"],
            fraud_score=prediction["ensemble_score"],
            is_fraudulent=prediction["is_fraudulent"],
            predicted_at=datetime.utcnow()
        )
        self.db.add(db_prediction)
        self.db.commit()
        self.db.refresh(db_prediction)
        return db_prediction

    def update_declaration_status(self, declaration_id: int, status: str):
        declaration = self.db.query(Declaration).filter(Declaration.id == declaration_id).first()
        if declaration:
            declaration.status = status
            self.db.commit()
            self.db.refresh(declaration)
        return declaration

    def create_audit_log(self, user_id: int | None, declaration_id: int, action: str, details: dict):
        db_audit = AuditLog(
            declaration_id=declaration_id,
            action=action,
            performed_by=user_id,
            performed_at=datetime.utcnow(),
            details=str(details)  # Convertit le dict en string pour stockage
        )
        self.db.add(db_audit)
        self.db.commit()
        self.db.refresh(db_audit)
        return db_audit

    def create_declaration(self, declaration: dict, user_id: int):
        db_declaration = Declaration(**declaration, user_id=user_id, status="pending")
        self.db.add(db_declaration)
        self.db.commit()
        self.db.refresh(db_declaration)
        return db_declaration

    def get_declarations(self, user_id: int):
        return self.db.query(Declaration).filter(Declaration.user_id == user_id).all()