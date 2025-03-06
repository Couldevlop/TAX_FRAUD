from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, ForeignKey, Boolean, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Declaration(Base):
    __tablename__ = "declarations"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    company_name = Column(String(255))
    declaration_type = Column(String(50), nullable=False)
    amount = Column(Float, nullable=False)
    sector = Column(String(100))
    region = Column(String(100))
    fiscal_year = Column(Integer, nullable=False)
    status = Column(String(50), default="pending")
    submitted_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")

class FraudPrediction(Base):
    __tablename__ = "fraud_predictions"
    
    id = Column(Integer, primary_key=True, index=True)
    declaration_id = Column(Integer, ForeignKey("declarations.id"), nullable=False)
    iso_forest_score = Column(Float)
    xgboost_score = Column(Float)
    neural_net_score = Column(Float)
    ensemble_score = Column(Float)
    is_fraudulent = Column(Boolean, default=False)
    analyzed_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")

class AuditLog(Base):
    __tablename__ = "audit_logs"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    declaration_id = Column(Integer, ForeignKey("declarations.id"))
    action = Column(String(100))
    details = Column(JSON)
    performed_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")