import sqlite3
import pandas as pd

# Connexion à la base de données
conn = sqlite3.connect("pme_ventes.db")
cursor = conn.cursor()

# Réinitialisation des tables pour test/démo (en phase dev)
cursor.execute("DROP TABLE IF EXISTS produits")
cursor.execute("DROP TABLE IF EXISTS magasins")
cursor.execute("DROP TABLE IF EXISTS ventes")

# Création des tables
cursor.execute("""
CREATE TABLE produits (
    id_ref_produit TEXT PRIMARY KEY,
    nom TEXT,
    prix REAL
)
""")

cursor.execute("""
CREATE TABLE magasins (
    id_magasin INTEGER PRIMARY KEY,
    ville TEXT
)
""")

cursor.execute("""
CREATE TABLE ventes (
    id_vente INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    id_ref_produit TEXT,
    quantite INTEGER,
    id_magasin INTEGER,
    FOREIGN KEY (id_ref_produit) REFERENCES produits(id_ref_produit),
    FOREIGN KEY (id_magasin) REFERENCES magasins(id_magasin)
)
""")
conn.commit()

# Chargement et préparation des CSV

# Produits
produits = pd.read_csv("Donnés brief data engineer - produits.csv")
produits.rename(columns={
    "ID Référence produit": "id_ref_produit",
    "Nom": "nom",
    "Prix": "prix"
}, inplace=True)
produits = produits[["id_ref_produit", "nom", "prix"]]

# Magasins
magasins = pd.read_csv("Donnés brief data engineer - magasins.csv")
magasins.rename(columns={
    "ID Magasin": "id_magasin",
    "Ville": "ville"
}, inplace=True)
magasins = magasins[["id_magasin", "ville"]]

# Ventes
ventes = pd.read_csv("Donnés brief data engineer - ventes.csv")
ventes.rename(columns={
    "Date": "date",
    "ID Référence produit": "id_ref_produit",
    "Quantité": "quantite",
    "ID Magasin": "id_magasin"
}, inplace=True)
ventes = ventes[["date", "id_ref_produit", "quantite", "id_magasin"]]

#  Insertion des données
produits.to_sql("produits", conn, if_exists="append", index=False)
magasins.to_sql("magasins", conn, if_exists="append", index=False)
ventes.to_sql("ventes", conn, if_exists="append", index=False)

print(f"✅ Données insérées avec succès :")
print(f"   - {len(produits)} produits")
print(f"   - {len(magasins)} magasins")
print(f"   - {len(ventes)} ventes")

conn.close()
