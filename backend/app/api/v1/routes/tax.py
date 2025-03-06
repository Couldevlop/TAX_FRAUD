from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.tax_schema import Declaration, DeclarationCreate
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

@router.post("/", response_model=Declaration)
def create_declaration(
    declaration: DeclarationCreate,
    db: Session = Depends(get_db)
):
    tax_service = TaxService(db)
    return tax_service.create_declaration(declaration, user_id=1)  # user_id temporaire

@router.get("/{declaration_id}", response_model=Declaration)
def get_declaration(
    declaration_id: int,
    db: Session = Depends(get_db)
):
    tax_service = TaxService(db)
    declaration = tax_service.repository.get_declaration_by_id(declaration_id)
    if not declaration:
        raise HTTPException(status_code=404, detail="Declaration not found")
    return declaration

@router.post("/generate/{count}", response_model=list[Declaration])
def generate_declarations(
    count: int,
    db: Session = Depends(get_db)
):
    tax_service = TaxService(db)
    return tax_service.generate_bulk_declarations(user_id=1, count=count)