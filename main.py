from database_interaction.crud import create_entry, read_entries, update_entry, delete_entry
from config.logging_config import setup_logger
from database_interaction.queries import queries

setup_logger()

def main():
    # Exemple de lecture d'entrées
    results = read_entries(queries["select_departments"])
    if results:
        for row in results:
            print("Department:", row)

    # Exemple de mise à jour d'une entrée
    # update_entry("UPDATE my_app_departments SET location = :1 WHERE department_name = :2", ("Lyon", "IT Department"))

    # Exemple de suppression d'une entrée
    # delete_entry("DELETE FROM my_app_departments WHERE department_name = :1", ("IT Department",))
if __name__ == "__main__":
    main()
