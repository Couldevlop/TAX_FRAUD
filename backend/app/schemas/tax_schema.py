from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class DeclarationCreate(BaseModel):
    user_id: int
    company_name: Optional[str]
    declaration_type: str
    amount: float
    sector: Optional[str]
    region: Optional[str]
    fiscal_year: int
    status: Optional[str] = "pending"

class Declaration(BaseModel):
    id: int
    user_id: int
    company_name: Optional[str]
    declaration_type: str
    amount: float
    sector: Optional[str]
    region: Optional[str]
    fiscal_year: int
    status: str
    submitted_at: datetime

    class Config:
        from_attributes = True  # Pydantic V2