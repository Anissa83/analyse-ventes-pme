# Utiliser une image de base légère avec Python
FROM python:3.10-slim

# Créer un dossier de travail dans le conteneur
WORKDIR /app

# Copier les dépendances (requirements.txt) et installer les packages
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copier tous les scripts Python
COPY Script/ ./Script

# Copier les fichiers CSV
# COPY "Donnees brief data engineer - produits.csv" ./
# COPY "Donnees brief data engineer - magasins.csv" ./
# COPY "Donnees brief data engineer - ventes.csv" ./
# COPY produits.csv ./
# COPY magasins.csv ./
# COPY ventes.csv ./

# Copier la base de données SQLite si elle existe (ou elle sera créée)
COPY pme_ventes.db ./

# Indiquer le script à lancer automatiquement (ici importation)
CMD ["python", "Script/import_data.py"]
