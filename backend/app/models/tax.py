from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from . import Base



class Declaration(Base):
    __tablename__ = "declarations"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    company_name = Column(String(255), nullable=True)
    declaration_type = Column(String(50), nullable=False, index=True)
    amount = Column(Float(15,2), nullable=False)  # Précision pour DECIMAL(15,2)
    sector = Column(String(100), nullable=True)
    region = Column(String(100), nullable=True)
    fiscal_year = Column(Integer, nullable=False)
    status = Column(String(50), default="pending")
    submitted_at = Column(DateTime(timezone=False), server_default=func.now())

class FraudPrediction(Base):
    __tablename__ = "fraud_predictions"
    id = Column(Integer, primary_key=True, index=True)
    declaration_id = Column(Integer, ForeignKey("declarations.id", ondelete="CASCADE"), index=True)
    fraud_score = Column(Float)
    is_fraudulent = Column(Boolean)
    predicted_at = Column(DateTime(timezone=False), server_default=func.now())

class AuditLog(Base):
    __tablename__ = "audit_logs"
    id = Column(Integer, primary_key=True, index=True)
    declaration_id = Column(Integer, ForeignKey("declarations.id", ondelete="CASCADE"), index=True)
    action = Column(String(100))
    performed_by = Column(Integer, ForeignKey("users.id"))  # user_id
    performed_at = Column(DateTime(timezone=False), server_default=func.now())