from fastapi import FastAPI
from app.api.v1.routes import tax, user, fraud
from app.core.config import settings
from app.models import Base
from sqlalchemy import create_engine

# Initialisation de la base de données
engine = create_engine(settings.DATABASE_URL)

def init_db():
    Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Tax Fraud Detection API",
    description="API pour la gestion et détection de fraude fiscale",
    version="1.0.0"
)

# Inclusion des routes
app.include_router(tax.router, prefix="/api/v1/tax", tags=["tax"])
app.include_router(user.router, prefix="/api/v1/user", tags=["user"])
app.include_router(fraud.router, prefix="/api/v1/fraud", tags=["fraud"])

@app.on_event("startup")
async def startup_event():
    init_db()

@app.get("/")
async def root():
    return {"message": "Welcome to Tax Fraud Detection API"}