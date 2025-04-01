import sqlite3
import os

# Connexion à la base SQLite
conn = sqlite3.connect("pme_ventes.db")
cursor = conn.cursor()

# --- Requête 1 : Chiffre d'affaires total ---
cursor.execute("""
SELECT SUM(v.quantite * p.prix) AS chiffre_affaires_total
FROM ventes v
JOIN produits p ON v.id_ref_produit = p.id_ref_produit
""")
ca_total = cursor.fetchone()[0] or 0

# --- Requête 2 : Top 5 produits les plus vendus ---
cursor.execute("""
SELECT p.nom, SUM(v.quantite) AS total_vendus
FROM ventes v
JOIN produits p ON v.id_ref_produit = p.id_ref_produit
GROUP BY p.nom
ORDER BY total_vendus DESC
LIMIT 5
""")
top_produits = cursor.fetchall()

# --- Requête 3 : Chiffre d'affaires par ville ---
cursor.execute("""
SELECT m.ville, SUM(v.quantite * p.prix) AS chiffre_affaires
FROM ventes v
JOIN produits p ON v.id_ref_produit = p.id_ref_produit
JOIN magasins m ON v.id_magasin = m.id_magasin
GROUP BY m.ville
ORDER BY chiffre_affaires DESC
""")
ca_villes = cursor.fetchall()

# --- Génération du fichier note_analyse.txt ---
os.makedirs("notes", exist_ok=True)  # Crée le dossier s'il n'existe pas

with open("notes/note_analyse.txt", "w", encoding="utf-8") as f:
    f.write("📊 Résumé des analyses - PME\n\n")

    f.write(f"1. 💰 Chiffre d'affaires total : {ca_total:.2f} €\n\n")

    f.write("2. 🏆 Top 5 produits les plus vendus :\n")
    for nom, total in top_produits:
        f.write(f"   - {nom} : {total} ventes\n")
    f.write("\n")

    f.write("3. 🗺️ Chiffre d'affaires par ville :\n")
    for ville, montant in ca_villes:
        f.write(f"   - {ville} : {montant:.2f} €\n")

print("✅ Résumé écrit dans notes/note_analyse.txt")

# Fermeture de la connexion
conn.close()
