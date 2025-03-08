import pandas as pd
import psycopg2
from datetime import datetime
import random
from passlib.context import CryptContext

# Configuration du hachage des mots de passe
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Fonction pour hacher un mot de passe
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# Connexion à la base de données
conn = psycopg2.connect(
    dbname="tax_db",
    user="user",
    password="123",
    host="db",
    port="5432"
)
cursor = conn.cursor()

print("Script démarré !")

# Insertion des utilisateurs
users = [
    (1, "test@example.com", "Test User", hash_password("123"), "user"),
    (2, "user2@example.com", "User Two", hash_password("123"), "user"),
    (3, "user3@example.com", "User Three", hash_password("123"), "user"),
    (4, "user4@example.com", "User Four", hash_password("123"), "user"),
    (5, "user5@example.com", "User Five", hash_password("123"), "user"),
]

try:
    cursor.executemany(
        """
        INSERT INTO users (id, email, full_name, hashed_password, role)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (id) DO NOTHING
        """,
        users
    )
    conn.commit()
    print("✅ 5 utilisateurs insérés avec succès.")
except Exception as e:
    conn.rollback()
    print(f"Erreur lors de l'insertion des utilisateurs : {e}")

# Génération des déclarations
print("Démarrage de la génération des déclarations...")
declarations = []
for _ in range(10000):
    user_id = random.randint(1, 5)
    company_name = f"Entreprise_{random.randint(10000, 99999)}"
    declaration_type = random.choice(["TVA", "ITS", "IR"])
    amount = round(random.uniform(1000, 10000000), 2)
    sector = random.choice(["Commerce", "Industrie", "Services"])
    region = random.choice(["Abidjan", "Bouaké", "Yamoussoukro"])
    fiscal_year = random.randint(2020, 2023)
    status = "pending"
    submitted_at = datetime.now()
    declarations.append((user_id, company_name, declaration_type, amount, sector, region, fiscal_year, status, submitted_at))

df = pd.DataFrame(declarations, columns=["user_id", "company_name", "declaration_type", "amount", "sector", "region", "fiscal_year", "status", "submitted_at"])
print("✅ Aperçu des données générées :")
print(df.head().to_string())

try:
    cursor.executemany(
        """
        INSERT INTO declarations (user_id, company_name, declaration_type, amount, sector, region, fiscal_year, status, submitted_at)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        declarations
    )
    conn.commit()
    print("✅ 10000 déclarations insérées avec succès.")
except Exception as e:
    conn.rollback()
    print(f"Erreur lors de l'insertion des déclarations : {e}")

print("Script terminé !")
cursor.close()
conn.close()