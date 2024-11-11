from database_interaction.logger_config import setup_logger
from database_interaction.execute import execute_query
from database_interaction.queries import queries  # Importe les requêtes

def main():
    setup_logger()

    # Utilisation des requêtes importées
    print("Départements :")
    execute_query(queries["select_departments"])

    print("\nEmployés :")
    execute_query(queries["select_employees"])

    print("\nProjets et employés assignés :")
    execute_query(queries["select_projects_and_employees"])

    print("\nSalaires des employés :")
    execute_query(queries["select_salaries"])

    print("\nManagers des départements :")
    execute_query(queries["select_departments_managers"])

    print("\nTest d'erreur :")
    execute_query(queries["select_non_existent_table"])

if __name__ == "__main__":
    main()
