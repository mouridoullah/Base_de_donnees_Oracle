# Projet Oracle Database Docker avec Grafana et Prometheus

Ce projet contient une configuration Docker pour exécuter une base de données Oracle avec un monitoring de performance via Prometheus et Grafana. Il inclut également des scripts d'interaction avec la base de données en Python et des scripts SQL pour initialiser et manipuler les données.

## Structure du Projet

```
.
├── .env
├── config
│   ├── db_config.py
│   ├── logging_config.py
│   └── __pycache__
│       ├── db_config.cpython-312.pyc
│       └── logging_config.cpython-312.pyc
├── create_project_structure.sh
├── database_interaction
│   ├── crud.py
│   ├── execute.py
│   ├── __init__.py
│   ├── populate_db.py
│   ├── __pycache__
│   │   ├── crud.cpython-312.pyc
│   │   ├── execute.cpython-312.pyc
│   │   ├── __init__.cpython-312.pyc
│   │   ├── queries.cpython-312.pyc
│   │   └── transactions.cpython-312.pyc
│   ├── queries.py
│   └── transactions.py
├── docker-compose.yml
├── Dockerfile
├── grafana
│   ├── dashboards
│   │   └── custom_dashboard.json
│   └── grafana.ini
├── LICENSE
├── logs
│   └── database_logs.log
├── main.py
├── prometheus
│   └── prometheus.yml
├── README.md
├── requirements.txt
├── scripts
│   ├── 01_create_tables.sql
│   ├── 02_insert_data.sql
│   └── 03_drop_tables.sql
├── struc
└── tests
    ├── __init__.py
    ├── test_config.py
    ├── test_crud.py
    ├── test_execute.py
    └── test_transactions.py
```

## Prérequis

- **Docker et Docker Compose** : Assurez-vous que Docker et Docker Compose sont installés.
- **Python 3.x** : Pour exécuter les scripts Python, installez les dépendances listées dans `requirements.txt`.

## Installation

1. Clonez le projet :
   ```bash
   git clone https://github.com/mouridoullah/Base_de_donnees_Oracle.git
   cd Base_de_donnees_Oracle
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