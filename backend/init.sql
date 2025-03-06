-- Table des utilisateurs (entreprises ou individus)
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    full_name VARCHAR(255) NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    role VARCHAR(50) DEFAULT 'user', -- user, admin, auditor
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table des déclarations fiscales
CREATE TABLE IF NOT EXISTS declarations (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    company_name VARCHAR(255),
    declaration_type VARCHAR(50) NOT NULL, -- 'income', 'vat', 'corporate'
    amount DECIMAL(15,2) NOT NULL,
    sector VARCHAR(100), -- 'tech', 'retail', 'manufacturing', etc.
    region VARCHAR(100),
    fiscal_year INT NOT NULL,
    status VARCHAR(50) DEFAULT 'pending', -- 'pending', 'approved', 'flagged', 'rejected'
    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Table des prédictions de fraude
CREATE TABLE IF NOT EXISTS fraud_predictions (
    id SERIAL PRIMARY KEY,
    declaration_id INT NOT NULL,
    iso_forest_score FLOAT, -- Score de l'Isolation Forest
    xgboost_score FLOAT, -- Score de XGBoost
    neural_net_score FLOAT, -- Score du réseau neuronal
    ensemble_score FLOAT, -- Score combiné
    is_fraudulent BOOLEAN DEFAULT FALSE,
    analyzed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (declaration_id) REFERENCES declarations(id) ON DELETE CASCADE
);

-- Table d'historique d'audit
CREATE TABLE IF NOT EXISTS audit_logs (
    id SERIAL PRIMARY KEY,
    user_id INT,
    declaration_id INT,
    action VARCHAR(100), -- 'created', 'updated', 'flagged', 'approved'
    details JSONB,
    performed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (declaration_id) REFERENCES declarations(id)
);