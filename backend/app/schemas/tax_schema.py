from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class DeclarationBase(BaseModel):
    company_name: Optional[str]
    declaration_type: str
    amount: float
    sector: Optional[str]
    region: Optional[str]
    fiscal_year: int

class DeclarationCreate(DeclarationBase):
    pass

class Declaration(DeclarationBase):
    id: int
    user_id: int
    status: str
    submitted_at: datetime

    class Config:
        orm_mode = True

class FraudPredictionBase(BaseModel):
    declaration_id: int
    iso_forest_score: Optional[float]
    xgboost_score: Optional[float]
    neural_net_score: Optional[float]
    ensemble_score: Optional[float]
    is_fraudulent: bool

class FraudPrediction(FraudPredictionBase):
    id: int
    analyzed_at: datetime

    class Config:
        orm_mode = True