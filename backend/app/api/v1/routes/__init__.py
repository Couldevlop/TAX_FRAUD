# Initialisation des routes API
from .tax import router as tax_router
from .user import router as user_router
from .fraud import router as fraud_router

__all__ = ["tax_router", "user_router", "fraud_router"]