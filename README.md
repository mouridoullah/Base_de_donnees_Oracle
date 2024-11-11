# Projet Oracle avec Docker

Ce projet crée une base de données Oracle via Docker, avec un schéma complet incluant des tables pour les départements, les employés, les projets, et les salaires. Les données sont insérées automatiquement lors du démarrage du conteneur à l'aide de scripts d'initialisation SQL.

## Structure du Projet

```
.
├── database_interaction.py      # Script Python pour interagir avec la base de données
├── docker-compose.yml           # Configuration Docker Compose pour lancer Oracle et les services associés
├── Dockerfile                   # Dockerfile pour créer l'image Docker Oracle
├── scripts                      # Répertoire contenant les scripts SQL d'initialisation
│   ├── 01_create_tables.sql     # Script de création des tables
│   ├── 02_insert_data.sql       # Script d'insertion des données
│   └── 03_drop_tables.sql       # Script pour supprimer les tables (utilisé pour réinitialiser la base)
└── .env                         # Fichier de configuration des variables d'environnement
```

## Prérequis

- Docker
- Docker Compose
- Python 3.x
- Oracle Client (pour l'interaction avec la base de données en Python)

## Configuration

Avant de démarrer le projet, vous devez configurer le fichier `.env` avec les valeurs appropriées pour la base de données Oracle. Un exemple de contenu pour le fichier `.env` :

```env
ORACLE_PASSWORD=monMotDePasse
DB_PORT=1521
EM_PORT=5500
ORACLE_SID=XE
ORACLE_PDB=ORCLPDB1
INIT_SGA_SIZE=1024
INIT_PGA_SIZE=256
ORACLE_CHARACTERSET=AL32UTF8
APP_USER=my_user
APP_USER_PASSWORD=monAppMotDePasse
```

## Installation et Démarrage

1. **Clonez le projet** :

   ```bash
   git clone https://github.com/mouridoullah/Base_de_donnees_Oracle.git
   cd Base_de_donnees_Oracle
   ```

2. **Construisez et démarrez les services Docker** :

   Utilisez Docker Compose pour construire l'image et démarrer les services.

   ```bash
   docker-compose up --build
   ```

   Ce processus téléchargera l'image Oracle, créera et initialisera la base de données avec les scripts SQL dans le répertoire `scripts`, et démarrera les services.

3. **Vérifiez l'état de la base de données** :

   Une fois les services démarrés, Oracle sera accessible à `localhost` sur le port 1521 (défini dans `.env`). Vous pouvez accéder à Oracle SQL Developer via le port 5500 pour gérer la base de données via une interface graphique.

## Interagir avec la base de données via Python

Le script `database_interaction.py` vous permet d'interagir avec la base de données Oracle à partir de Python. Vous pouvez l'utiliser pour consulter les données des tables ou exécuter des requêtes SQL. Voici un exemple de code pour récupérer et afficher les employés :

```python
import oracledb

try:
    connection = oracledb.connect(
        user="SYS",
        password="monMotDePasse",
        dsn="localhost:1521/XE",  
        mode=oracledb.SYSDBA
    )

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM my_app_employees")
    for row in cursor:
        print(row)
    cursor.close()
    connection.close()

except oracledb.DatabaseError as e:
    print("Erreur lors de la connexion ou de l'exécution de la requête :", e)
```

### Dépendances Python

Installez les dépendances nécessaires pour interagir avec Oracle depuis Python :

```bash
pip install oracledb
```

## Fonctionnalités du Projet

- **Dockerisation d'Oracle** : Ce projet met en place un environnement Oracle XE (Express Edition) dans un conteneur Docker.
- **Initialisation automatisée de la base de données** : Les scripts SQL dans `scripts/` sont exécutés automatiquement lors du démarrage du conteneur, créant les tables et insérant des données.
- **Interaction avec la base de données** : Utilisation de Python pour exécuter des requêtes SQL et afficher les résultats.

## Comment arrêter les services

Pour arrêter le projet et les conteneurs Docker, vous pouvez utiliser la commande suivante :

```bash
docker-compose down
```

Cela arrêtera et supprimera les conteneurs, mais les données seront conservées à moins que vous ne choisissiez de supprimer les volumes avec la commande :

```bash
docker-compose down -v
```

## Contribution

Si vous souhaitez contribuer à ce projet, vous pouvez fork ce repository et proposer des modifications via des pull requests.

## Auteurs

- **mouridoullah** – *mn*

## Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.


### Points à personnaliser :
- **Liens et auteur** : Adaptez les liens vers votre profil GitHub ou d'autres informations de contact.
- **Dépendances** : Assurez-vous que toutes les dépendances nécessaires (comme le module `oracledb`) sont installées dans votre environnement Python.