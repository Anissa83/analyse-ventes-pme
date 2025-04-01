# 📊 Analyse des Ventes d'une PME - Projet Data Engineer

Projet réalisé dans le cadre du brief Simplon pour l’analyse des ventes d'une PME à partir de données brutes (CSV).  
Il utilise Python, SQLite et Docker pour construire un pipeline complet d'importation, d'analyse et de visualisation des données.

---

## 📂 Contenu du projet

- `Script/import_data.py` : Script Python pour importer les données CSV dans une base SQLite
- `Script/analyse_sql.py` : Script Python pour exécuter les requêtes d’analyse SQL
- `notes/note_analyse.txt` : Résumé écrit des résultats d’analyse
- `mcd.md` + `mcd.png` : Schéma conceptuel de la base (MCD)
- `Docker/Dockerfile` : Image Docker pour exécuter les scripts Python
- `docker-compose.yml` : Orchestration des services avec Docker
- `requirements.txt` : Liste des packages Python à installer
- `pme_ventes.db` : Base de données SQLite générée

---

## 🚀 Comment exécuter le projet

### ▶️ Option 1 : En local avec Python

1. Assurez-vous d’avoir Python 3.x installé
2. Installez les dépendances :
```bash
pip install -r requirements.txt
