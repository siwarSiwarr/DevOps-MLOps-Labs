# Image de base Python 3.12
FROM python:3.12-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier requirements.txt
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copier SEULEMENT le code source
COPY src/ ./src/

# Créer le dossier models
RUN mkdir -p models

# Commande par défaut: entraîner le modèle
CMD ["python", "src/train.py"]