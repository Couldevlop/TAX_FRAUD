# Initialisation des schémas
from .tax_schema import (
    DeclarationBase, DeclarationCreate, Declaration,
    FraudPredictionBase, FraudPrediction
)

__all__ = [
    "DeclarationBase", "DeclarationCreate", "Declaration",
    "FraudPredictionBase", "FraudPrediction"
]