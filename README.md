# Projet Oracle Database Docker avec Grafana et Prometheus

Ce projet contient une configuration Docker pour exécuter une base de données Oracle avec un monitoring de performance via Prometheus et Grafana. Il inclut également des scripts d'interaction avec la base de données en Python et des scripts SQL pour initialiser et manipuler les données.

## Structure du Projet

```
.
├── database_interaction
│   ├── config.py                 # Configuration de la base de données
│   ├── execute.py                # Exécution des requêtes SQL
│   ├── __init__.py               # Fichier d'initialisation de module
│   ├── logger_config.py          # Configuration du système de logs
│   ├── manage_transaction.py     # Gestion des transactions SQL
│   ├── queries.py                # Requêtes SQL
│   └── __pycache__               # Cache Python compilé
├── database_interaction.py       # Script principal pour l'interaction DB
├── docker-compose.yml            # Configuration Docker Compose
├── Dockerfile                    # Dockerfile pour Oracle Database
├── LICENSE                       # Licence du projet
├── logs
│   └── database_logs.log         # Fichier de logs pour les transactions SQL
├── main.py                       # Point d'entrée principal du projet
├── prometheus
│   └── prometheus.yml            # Configuration de Prometheus
├── prometheus.yml                # Fichier de configuration pour Prometheus
├── README.md                     # Documentation du projet
├── requirements.txt              # Dépendances Python
├── scripts
│   ├── 01_create_tables.sql      # Script SQL de création de tables
│   ├── 02_insert_data.sql        # Script SQL d'insertion de données
│   └── 03_drop_tables.sql        # Script SQL pour supprimer des tables
└── teste
    ├── __init__.py               # Fichier d'initialisation de module de test
    ├── test_config.py            # Tests pour config.py
    ├── test_execute.py           # Tests pour execute.py
    └── test_manage_transaction.py# Tests pour manage_transaction.py
```

## Prérequis

- **Docker et Docker Compose** : Assurez-vous que Docker et Docker Compose sont installés.
- **Python 3.x** : Pour exécuter les scripts Python, installez les dépendances listées dans `requirements.txt`.

## Installation

1. Clonez le projet :
   ```bash
   git clone <url_du_projet>
   cd <nom_du_projet>
   ```

2. Configurez les variables d'environnement dans le fichier `.env` :
   ```plaintext
   DB_USER=SYS
   DB_PASSWORD=monMotDePasse
   DB_DSN=localhost:1521/XE
   DB_PORT=1521
   EM_PORT=5500
   ORACLE_SID=XE
   ORACLE_PDB=ORCLPDB1
   INIT_SGA_SIZE=1024
   INIT_PGA_SIZE=256
   ORACLE_CHARACTERSET=AL32UTF8
   ```

3. Installez les dépendances Python :
   ```bash
   pip install -r requirements.txt
   ```

## Lancement du Projet

1. Lancez les services Docker :
   ```bash
   docker-compose up -d
   ```

2. Accédez aux services :
   - **Base de données Oracle** : accessible sur `localhost:${DB_PORT}`.
   - **Prometheus** : accessible sur `http://localhost:9090`.
   - **Grafana** : accessible sur `http://localhost:3000` (utilisateur par défaut : `admin`, mot de passe : `admin`).

## Utilisation

### Interactions avec la base de données

- Utilisez `database_interaction.py` pour exécuter des requêtes SQL et interagir avec la base de données.
- Exécutez le script principal `main.py` pour tester l'accès aux tables et afficher les données dans la console :

   ```bash
   python main.py
   ```

### Monitoring des Performances avec Grafana et Prometheus

1. **Ajout de la source de données Prometheus dans Grafana** :
   - Allez dans **Configuration > Data Sources > Add data source**.
   - Sélectionnez **Prometheus** et définissez l'URL comme `http://prometheus:9090`.

2. **Tableaux de bord Grafana** :
   - Importez un tableau de bord Oracle prédéfini dans Grafana via **Dashboards > Import**.
   - Recherchez un tableau de bord Oracle ou importez en utilisant l'ID.

## Scripts SQL

- Les scripts dans le dossier `scripts` sont montés automatiquement dans le conteneur Oracle et exécutés au démarrage.
   - **01_create_tables.sql** : Crée les tables nécessaires.
   - **02_insert_data.sql** : Insère les données de base dans les tables.
   - **03_drop_tables.sql** : Supprime les tables pour un nettoyage complet.

## Tests

Les tests unitaires pour les modules d'interaction avec la base de données sont dans le dossier `teste` et peuvent être exécutés avec `pytest` :

```bash
pytest teste/
```

## Logs

Les logs des transactions SQL sont enregistrés dans `logs/database_logs.log`. Ils permettent de suivre les actions et de capturer les erreurs éventuelles.

---

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.