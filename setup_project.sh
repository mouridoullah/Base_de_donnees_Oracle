#!/bin/bash

# Définir la racine du projet
PROJECT_DIR="projet-base-de-donnees"

# Créer l'arborescence des répertoires
mkdir -p "$PROJECT_DIR/docs/documentation"
mkdir -p "$PROJECT_DIR/scripts/sql"
mkdir -p "$PROJECT_DIR/scripts/sauvegarde"
mkdir -p "$PROJECT_DIR/scripts/maintenance"
mkdir -p "$PROJECT_DIR/docker"
mkdir -p "$PROJECT_DIR/logs"
mkdir -p "$PROJECT_DIR/tests"

# Création des fichiers dans docs/documentation
echo "### Architecture de la base de données
- **Modèle logique et physique** : Les entités sont définies dans un diagramme ER et leur implémentation physique est décrite.
- **Configuration d'administration** : Paramètres recommandés pour la base de données Oracle, y compris la mémoire, la gestion des utilisateurs et des tablespaces.
- **Sécurité** : Recommandations pour la gestion des privilèges et des rôles, ainsi que le chiffrement des données.

" > "$PROJECT_DIR/docs/documentation/architecture.md"

echo "### Manuel Utilisateur
1. Connexion à la base de données
2. Requêtes de base pour accéder et modifier les données
3. Gestion des erreurs courantes

" > "$PROJECT_DIR/docs/documentation/utilisateur.md"

# Création des fichiers dans scripts/sql
echo "/* Script de création des tables et insertion des données */" > "$PROJECT_DIR/scripts/sql/creation_et_insertion.sql"
echo "/* Script pour index et analyse de performance */" > "$PROJECT_DIR/scripts/sql/index_et_performance.sql"

# Création des fichiers dans scripts/sauvegarde
echo "#! /bin/bash

# Sauvegarde de la base de données avec RMAN
rman target / <<EOF
backup database;
EOF

# Si argument restore est fourni, restaurer la base de données
if [ \"\$1\" == \"restore\" ]; then
    rman target / <<EOF
    restore database;
    recover database;
EOF
fi
" > "$PROJECT_DIR/scripts/sauvegarde/gestion.sh"
chmod +x "$PROJECT_DIR/scripts/sauvegarde/gestion.sh"

# Création des fichiers dans scripts/maintenance
echo "/* Script d'entretien : maintenance des index, analyse de performance et nettoyage des données */" > "$PROJECT_DIR/scripts/maintenance/entretien.sql"

# Création des fichiers dans docker
echo "FROM oracle/database:19.3.0-ee

# Variables d'environnement pour configurer la base de données
ENV ORACLE_SID=ORCL
ENV ORACLE_PDB=PDB1
ENV ORACLE_PASSWORD=Oracle_123

# Exposer les ports nécessaires
EXPOSE 1521 5500
" > "$PROJECT_DIR/docker/Dockerfile"

echo "version: '3.8'

services:
  oracle-db:
    build: .
    container_name: oracle-db
    environment:
      - ORACLE_SID=ORCL
      - ORACLE_PDB=PDB1
      - ORACLE_PASSWORD=Oracle_123
    ports:
      - 1521:1521
      - 5500:5500
    volumes:
      - ./data:/opt/oracle/oradata
      - ./init-db.sql:/docker-entrypoint-initdb.d/init-db.sql
    networks:
      - oracle-net

networks:
  oracle-net:
    driver: bridge
" > "$PROJECT_DIR/docker/docker-compose.yml"

echo "/* Script d'initialisation de la base de données et des utilisateurs */" > "$PROJECT_DIR/docker/init-db.sql"

# Création des fichiers dans logs
touch "$PROJECT_DIR/logs/db.log"

# Création des fichiers dans tests
echo "/* Tests d'intégration et de validation des fonctionnalités de la base de données */" > "$PROJECT_DIR/tests/validation.sql"

# Confirmation de la création
echo "L'architecture du projet a été créée avec succès !"
