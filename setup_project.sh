#!/bin/bash

# Définir la structure du projet
BASE_DIR="oracle-db-project"

# Créer les répertoires
mkdir -p $BASE_DIR/docker
mkdir -p $BASE_DIR/docker/env
mkdir -p $BASE_DIR/sql/schema
mkdir -p $BASE_DIR/sql/data
mkdir -p $BASE_DIR/sql/procedures
mkdir -p $BASE_DIR/backup
mkdir -p $BASE_DIR/config
mkdir -p $BASE_DIR/logs
mkdir -p $BASE_DIR/doc
mkdir -p $BASE_DIR/tests

# Créer les fichiers nécessaires
touch $BASE_DIR/docker/Dockerfile
touch $BASE_DIR/docker/docker-compose.yml
touch $BASE_DIR/docker/env/oracle.env
touch $BASE_DIR/sql/schema/create_tables.sql
touch $BASE_DIR/sql/schema/constraints.sql
touch $BASE_DIR/sql/data/insert_data.sql
touch $BASE_DIR/sql/procedures/example_proc.sql
touch $BASE_DIR/backup/full_backup.sh
touch $BASE_DIR/backup/incremental_backup.sh
touch $BASE_DIR/backup/restore.sh
touch $BASE_DIR/config/init.sql
touch $BASE_DIR/doc/schema_design.md
touch $BASE_DIR/doc/admin_guide.md
touch $BASE_DIR/doc/user_manual.md
touch $BASE_DIR/tests/unit_tests.sql
touch $BASE_DIR/tests/performance_tests.sql

# Ajouter un contenu de base aux fichiers
echo "# Dockerfile" > $BASE_DIR/docker/Dockerfile
echo "# docker-compose.yml" > $BASE_DIR/docker/docker-compose.yml
echo "# Oracle environment variables" > $BASE_DIR/docker/env/oracle.env
echo "-- Création des tables" > $BASE_DIR/sql/schema/create_tables.sql
echo "-- Contrainte des tables" > $BASE_DIR/sql/schema/constraints.sql
echo "-- Insertion de données" > $BASE_DIR/sql/data/insert_data.sql
echo "-- Exemple de procédure stockée" > $BASE_DIR/sql/procedures/example_proc.sql
echo "# Script de sauvegarde complète" > $BASE_DIR/backup/full_backup.sh
echo "# Script de sauvegarde incrémentielle" > $BASE_DIR/backup/incremental_backup.sh
echo "# Script de restauration" > $BASE_DIR/backup/restore.sh
echo "-- Script d'initialisation de la base de données Oracle" > $BASE_DIR/config/init.sql
echo "# Conception du schéma" > $BASE_DIR/doc/schema_design.md
echo "# Guide d'administration" > $BASE_DIR/doc/admin_guide.md
echo "# Manuel utilisateur" > $BASE_DIR/doc/user_manual.md
echo "-- Tests unitaires" > $BASE_DIR/tests/unit_tests.sql
echo "-- Tests de performance" > $BASE_DIR/tests/performance_tests.sql

# Message de fin
echo "Architecture du projet créée avec succès dans le répertoire $BASE_DIR"
