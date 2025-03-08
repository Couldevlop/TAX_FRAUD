from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from app.models.tax import Declaration as DeclarationModel
from app.schemas.tax_schema import Declaration as DeclarationSchema, DeclarationCreate
from app.services.tax_service import TaxService
from app.core.database import get_db
from app.core.security import get_current_user
from app.models.user import User

router = APIRouter(prefix="/tax", tags=["tax"])

@router.post("/upload", response_model=list[DeclarationSchema])
def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    tax_service = TaxService(db)
    data = [{"company_name": "Test", "declaration_type": "income", "amount": 10000, "fiscal_year": 2023}]
    declarations = [tax_service.create_declaration(DeclarationCreate(**item), current_user.id) for item in data]
    return declarations

@router.post("/", response_model=DeclarationSchema)
def create_declaration(declaration: DeclarationCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    tax_service = TaxService(db)
    return tax_service.create_declaration(declaration, user_id=current_user.id)

@router.get("/", response_model=list[DeclarationSchema])
async def get_declarations(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    tax_service = TaxService(db)
    return tax_service.get_declarations(current_user.id)