# Utilisation de l'image Oracle XE 11g
FROM oracleinanutshell/oracle-xe-11g:latest

# Définir les variables d’environnement par défaut
ENV ORACLE_HOME=/u01/app/oracle/product/11.2.0/xe
ENV PATH=$PATH:$ORACLE_HOME/bin
ENV ORACLE_SID=XE

EXPOSE 1521 5500

# Créer les répertoires pour persister les données et configurer les scripts d’initialisation
RUN mkdir -p /opt/oracle/oradata /docker-entrypoint-initdb.d
VOLUME /opt/oracle/oradata

# Copier les scripts initiaux pour l'initialisation de la base
COPY sql/schema /docker-entrypoint-initdb.d/schema
COPY sql/data /docker-entrypoint-initdb.d/data
COPY sql/procedures /docker-entrypoint-initdb.d/procedures
COPY config/init.sql /docker-entrypoint-initdb.d/
