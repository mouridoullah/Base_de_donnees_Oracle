import logging
import sys
import os
from faker import Faker
import random

# Ajouter le chemin du dossier parent au sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database_interaction.crud import create_entry
from config.logging_config import setup_logger

# Configurer les logs
setup_logger()
fake = Faker()

def populate_departments():
    logging.info("Insertion des départements...")
    for _ in range(10):
        department_name = fake.company()
        location = fake.city()
        create_entry(
            "INSERT INTO my_app_departments (department_name, location) VALUES (:1, :2)",
            (department_name, location)
        )

def populate_employees():
    logging.info("Insertion des employés...")
    for _ in range(50):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        hire_date = fake.date_this_decade()
        department_id = random.randint(1, 10)  # Assuming we have 10 departments inserted
        create_entry(
            "INSERT INTO my_app_employees (first_name, last_name, email, hire_date, department_id) VALUES (:1, :2, :3, :4, :5)",
            (first_name, last_name, email, hire_date, department_id)
        )

def populate_projects():
    logging.info("Insertion des projets...")
    for _ in range(20):
        project_name = fake.catch_phrase()
        start_date = fake.date_this_decade()
        end_date = fake.date_between(start_date=start_date)
        budget = random.randint(10000, 500000)
        create_entry(
            "INSERT INTO my_app_projects (project_name, start_date, end_date, budget) VALUES (:1, :2, :3, :4)",
            (project_name, start_date, end_date, budget)
        )

def populate_employee_projects():
    logging.info("Insertion des relations employé-projet...")
    for _ in range(50):
        employee_id = random.randint(1, 50)
        project_id = random.randint(1, 20)
        start_date = fake.date_this_decade()
        end_date = fake.date_between(start_date=start_date)
        create_entry(
            "INSERT INTO my_app_employee_projects (employee_id, project_id, start_date, end_date) VALUES (:1, :2, :3, :4)",
            (employee_id, project_id, start_date, end_date)
        )

def populate_salaries():
    logging.info("Insertion des salaires...")
    for _ in range(50):
        employee_id = random.randint(1, 50)
        salary_amount = random.randint(30000, 150000)
        start_date = fake.date_this_decade()
        end_date = fake.date_between(start_date=start_date)
        create_entry(
            "INSERT INTO my_app_salaries (employee_id, salary_amount, start_date, end_date) VALUES (:1, :2, :3, :4)",
            (employee_id, salary_amount, start_date, end_date)
        )

def populate_department_managers():
    logging.info("Insertion des managers de département...")
    for department_id in range(1, 11):
        manager_id = random.randint(1, 50)
        start_date = fake.date_this_decade()
        create_entry(
            "INSERT INTO my_app_departments_managers (department_id, manager_id, start_date) VALUES (:1, :2, :3)",
            (department_id, manager_id, start_date)
        )

def main():
    try:
        populate_departments()
        populate_employees()
        populate_projects()
        populate_employee_projects()
        populate_salaries()
        populate_department_managers()
        logging.info("Database population completed successfully.")
    except Exception as e:
        logging.error(f"Erreur lors de la population de la base de données : {e}")

if __name__ == "__main__":
    main()
