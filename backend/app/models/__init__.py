from sqlalchemy.ext.declarative import declarative_base

# Créer une base unifiée pour tous les modèles
Base = declarative_base()

from .user import User
from .tax import Declaration, FraudPrediction, AuditLog

__all__ = ["User", "Declaration", "FraudPrediction", "AuditLog", "Base"]