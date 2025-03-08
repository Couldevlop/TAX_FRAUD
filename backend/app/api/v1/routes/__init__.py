# Initialisation des routes API
from .tax import router as tax
from .user import router as user
from .fraud import router as fraud

__all__ = ["tax", "user", "fraud"]