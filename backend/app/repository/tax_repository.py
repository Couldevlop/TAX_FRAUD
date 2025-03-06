from sqlalchemy.orm import Session
from app.models.tax import Declaration, FraudPrediction, AuditLog
from app.schemas.tax_schema import DeclarationCreate

class TaxRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_declaration(self, declaration: DeclarationCreate, user_id: int) -> Declaration:
        db_declaration = Declaration(**declaration.dict(), user_id=user_id)
        self.db.add(db_declaration)
        self.db.commit()
        self.db.refresh(db_declaration)
        return db_declaration

    def get_declaration_by_id(self, declaration_id: int) -> Declaration:
        return self.db.query(Declaration).filter(Declaration.id == declaration_id).first()

    def get_declarations_by_user(self, user_id: int) -> list[Declaration]:
        return self.db.query(Declaration).filter(Declaration.user_id == user_id).all()

    def update_declaration_status(self, declaration_id: int, status: str) -> Declaration:
        declaration = self.get_declaration_by_id(declaration_id)
        if declaration:
            declaration.status = status
            self.db.commit()
            self.db.refresh(declaration)
        return declaration

    def create_fraud_prediction(self, prediction: dict) -> FraudPrediction:
        db_prediction = FraudPrediction(**prediction)
        self.db.add(db_prediction)
        self.db.commit()
        self.db.refresh(db_prediction)
        return db_prediction

    def create_audit_log(self, user_id: int, declaration_id: int, action: str, details: dict) -> AuditLog:
        db_log = AuditLog(user_id=user_id, declaration_id=declaration_id, action=action, details=details)
        self.db.add(db_log)
        self.db.commit()
        self.db.refresh(db_log)
        return db_log