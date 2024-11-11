import os
import oracledb
import logging
from dotenv import load_dotenv

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

# Configuration des logs
logging.basicConfig(
    filename='logs/database_logs.log',  # Fichier de logs
    level=logging.INFO,  # Niveau de log
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Paramètres de connexion (extraits des variables d'environnement)
db_config = {
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "dsn": os.getenv("DB_DSN"),
    "mode": oracledb.SYSDBA  # Mode sysdba si nécessaire
}

# Fonction pour exécuter une requête SQL et afficher les résultats
def execute_query(query):
    connection = None
    cursor = None
    try:
        logging.info("Connexion à la base de données...")
        connection = oracledb.connect(**db_config)
        cursor = connection.cursor()

        logging.info(f"Exécution de la requête : {query}")
        cursor.execute(query)

        # Récupération des résultats
        results = cursor.fetchall()
        for row in results:
            print(row)

        logging.info("Requête exécutée avec succès.")
        connection.commit()  # Commit des transactions

    except oracledb.DatabaseError as e:
        if connection is not None:
            connection.rollback()  # Rollback en cas d'erreur
        error_msg = f"Erreur lors de l'exécution de la requête : {e}"
        print(error_msg)
        logging.error(error_msg)

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()
        logging.info("Connexion à la base de données fermée.")

# Exemple de requêtes pour tester l'accès aux données
# 1. Afficher tous les départements
print("Départements :")
execute_query("SELECT * FROM my_app_departments")

# 2. Afficher tous les employés
print("\nEmployés :")
execute_query("SELECT * FROM my_app_employees")

# 3. Afficher les projets et les employés qui y participent
print("\nProjets et employés assignés :")
execute_query("""
    SELECT p.project_name, e.first_name || ' ' || e.last_name AS employee_name
    FROM my_app_projects p
    JOIN my_app_employee_projects ep ON p.project_id = ep.project_id
    JOIN my_app_employees e ON ep.employee_id = e.employee_id
""")

# 4. Afficher les salaires des employés
print("\nSalaires des employés :")
execute_query("""
    SELECT e.first_name || ' ' || e.last_name AS employee_name, s.salary_amount, s.start_date
    FROM my_app_salaries s
    JOIN my_app_employees e ON s.employee_id = e.employee_id
""")

# 5. Afficher les managers des départements
print("\nManagers des départements :")
execute_query("""
    SELECT d.department_name, e.first_name || ' ' || e.last_name AS manager_name
    FROM my_app_departments_managers dm
    JOIN my_app_departments d ON dm.department_id = d.department_id
    JOIN my_app_employees e ON dm.manager_id = e.employee_id
""")

# Exemple de requête pour tester la gestion des erreurs
# print("\nTest d'erreur :")
# execute_query("SELECT * FROM table_inexistante")
