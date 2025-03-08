from sqlalchemy.orm import Session
from app.schemas.tax_schema import DeclarationCreate
from app.repository.tax_repository import TaxRepository

class TaxService:
    def __init__(self, db: Session):
        self.repository = TaxRepository(db)

    def create_declaration(self, declaration: DeclarationCreate, user_id: int):
        return self.repository.create_declaration(declaration.dict(), user_id)

    def get_declarations(self, user_id: int):
        return self.repository.get_declarations(user_id)