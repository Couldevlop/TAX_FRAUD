from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base  # Importe la base unifiée
from app.core.config import settings  # Importe l'instance settings
from app.api.v1.routes import tax, user, fraud

# Initialisation de l'application FastAPI
app = FastAPI(title="Tax Fraud Detection API")

# Configuration de la base de données
engine = create_engine(settings.DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """
    Initialise la base de données en créant toutes les tables définies dans les modèles.
    """
    try:
        print("Tentative de création des tables...")
        Base.metadata.create_all(bind=engine)  # Crée toutes les tables (users, declarations, etc.)
        print("✅ Base de données initialisée avec succès.")
    except Exception as e:
        print(f"❌ Erreur lors de l'initialisation de la base de données : {e}")
        raise

# Événement de démarrage pour initialiser la base de données
@app.on_event("startup")
async def startup_event():
    init_db()

# Inclusion des routeurs
app.include_router(tax, prefix="/api/v1")
app.include_router(user, prefix="/api/v1/user")
app.include_router(fraud, prefix="/api/v1")

# Route de test
@app.get("/")
def read_root():
    return {"message": "Tax Fraud Detection API is running!"}