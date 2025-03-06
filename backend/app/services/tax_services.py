from sqlalchemy.orm import Session
from app.repositories.tax_repository import TaxRepository
from app.schemas.tax_schema import DeclarationCreate
from faker import Faker
import random

fake = Faker()

class TaxService:
    def __init__(self, db: Session):
        self.repository = TaxRepository(db)

    def create_declaration(self, declaration: DeclarationCreate, user_id: int):
        declaration = self.repository.create_declaration(declaration, user_id)
        self.repository.create_audit_log(user_id, declaration.id, "created", {"details": "New declaration submitted"})
        return declaration

    @staticmethod
    def generate_random_declaration(user_id: int) -> DeclarationCreate:
        amount = random.uniform(10000, 1000000)
        declaration_type = random.choice(["income", "vat", "corporate"])
        sector = random.choice(["tech", "retail", "manufacturing", "services"])
        region = fake.state()
        
        return DeclarationCreate(
            company_name=fake.company(),
            declaration_type=declaration_type,
            amount=amount,
            sector=sector,
            region=region,
            fiscal_year=2023
        )

    def generate_bulk_declarations(self, user_id: int, count: int = 1000):
        declarations = []
        for _ in range(count):
            declaration = self.create_declaration(self.generate_random_declaration(user_id), user_id)
            declarations.append(declaration)
        return declarations