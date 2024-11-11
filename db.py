import oracledb

# Paramètres de connexion (à adapter à ton fichier .env ou à ta configuration)
db_config = {
    "user": "SYS",
    "password": "monMotDePasse",
    "dsn": "localhost:1521/XE",  # Remplace par ton dsn ou utilise ORCLPDB1 si c'est le PDB
    "mode": oracledb.SYSDBA  # Mode sysdba si nécessaire
}

# Fonction pour exécuter une requête SQL et afficher les résultats
def execute_query(query):
    try:
        # Connexion à la base de données
        connection = oracledb.connect(**db_config)
        cursor = connection.cursor()

        # Exécution de la requête
        cursor.execute(query)
        
        # Récupération et affichage des résultats
        results = cursor.fetchall()
        for row in results:
            print(row)
        
        cursor.close()
        connection.close()
    except oracledb.DatabaseError as e:
        print("Erreur lors de l'exécution de la requête :", e)

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
