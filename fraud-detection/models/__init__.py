# Initialisation du module models
from .train_model import train_models
from .predict import FraudPredictor

__all__ = ["train_models", "FraudPredictor"]