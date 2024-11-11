queries = {
    "select_departments": "SELECT * FROM my_app_departments",
    "select_employees": "SELECT * FROM my_app_employees",
    "select_projects_and_employees": """
        SELECT p.project_name, e.first_name || ' ' || e.last_name AS employee_name
        FROM my_app_projects p
        JOIN my_app_employee_projects ep ON p.project_id = ep.project_id
        JOIN my_app_employees e ON ep.employee_id = e.employee_id
    """,
    "select_salaries": """
        SELECT e.first_name || ' ' || e.last_name AS employee_name, s.salary_amount, s.start_date
        FROM my_app_salaries s
        JOIN my_app_employees e ON s.employee_id = e.employee_id
    """,
    "select_departments_managers": """
        SELECT d.department_name, e.first_name || ' ' || e.last_name AS manager_name
        FROM my_app_departments_managers dm
        JOIN my_app_departments d ON dm.department_id = d.department_id
        JOIN my_app_employees e ON dm.manager_id = e.employee_id
    """,
    "select_non_existent_table": "SELECT * FROM table_inexistante",
    # Ajoute d'autres requêtes ici selon tes besoins
}
