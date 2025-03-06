from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.fraud_service import FraudService
from app.services.tax_service import TaxService
from app.core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

router = APIRouter()

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/check/{declaration_id}")
async def check_fraud(
    declaration_id: int,
    db: Session = Depends(get_db)
):
    tax_service = TaxService(db)
    declaration = tax_service.repository.get_declaration_by_id(declaration_id)
    if not declaration:
        raise HTTPException(status_code=404, detail="Declaration not found")
    
    fraud_service = FraudService(db)
    return await fraud_service.detect_fraud(declaration)