# Projet Base de Données

## Description
Ce projet vise à concevoir, déployer et administrer une base de données relationnelle complexe en utilisant Oracle et Docker. Il comprend des scripts SQL, des scripts de maintenance, et des procédures de sauvegarde et de restauration.

## Structure du Projet
La structure du projet est organisée comme suit :

```plaintext
projet-base-de-donnees/
│
├── docs/
│   ├── conception/
│   │   ├── diagramme-er.pdf
│   │   ├── modele-logique.pdf
│   │   └── modele-physique.pdf
│   ├── manuel-administration/
│   │   ├── installation.md
│   │   ├── configuration.md
│   │   └── securite.md
│   └── manuels-utilisateur/
│       ├── manuel-utilisateur.pdf
│       └── FAQ.md
│
├── scripts/
│   ├── sql/
│   │   ├── creation_tables.sql
│   │   ├── insertion_donnees.sql
│   │   └── index.sql
│   ├── sauvegarde/
│   │   ├── backup.sh
│   │   └── restore.sh
│   └── maintenance/
│       ├── maintenance_indexes.sql
│       ├── analyse_performance.sql
│       └── nettoyage_donnees.sql
│
├── docker/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── init-scripts/
│       ├── init-db.sql
│       └── init-users.sql
│
├── logs/
│   ├── access.log
│   ├── error.log
│   └── backup.log
│
├── tests/
│   ├── unittests.sql
│   ├── performance_tests.sql
│   └── integration_tests.sql
│
└── README.md
