import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from xgboost import XGBClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
import joblib

def train_models(data: pd.DataFrame, save_path: str = "models/"):
    """
    Entraîne trois modèles de détection de fraude et les sauvegarde.
    """
    # Préparation des features
    X = data[['amount', 'fiscal_year']]
    # Label binaire simulé (à remplacer par des données réelles si disponibles)
    y = (data['amount'] < data['amount'].mean() * 0.5).astype(int)  # Simulation de fraude

    # Normalisation des données
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # 1. Isolation Forest
    iso_forest = IsolationForest(contamination=0.1, random_state=42)
    iso_forest.fit(X_scaled)
    joblib.dump(iso_forest, f"{save_path}iso_forest.pkl")
    joblib.dump(scaler, f"{save_path}scaler.pkl")

    # 2. XGBoost
    xgb = XGBClassifier(random_state=42)
    xgb.fit(X_scaled, y)
    joblib.dump(xgb, f"{save_path}xgboost.pkl")

    # 3. Neural Network
    nn = MLPClassifier(hidden_layer_sizes=(64, 32), max_iter=500, random_state=42)
    nn.fit(X_scaled, y)
    joblib.dump(nn, f"{save_path}neural_net.pkl")

    return {"iso_forest": iso_forest, "xgboost": xgb, "neural_net": nn, "scaler": scaler}

if __name__ == "__main__":
    # Exemple de données pour tester
    data = pd.DataFrame({
        'amount': np.random.uniform(10000, 1000000, 1000),
        'fiscal_year': np.random.randint(2020, 2024, 1000)
    })
    train_models(data)