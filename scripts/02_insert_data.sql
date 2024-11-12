-- -- Insertion des départements
-- INSERT INTO my_app_departments (department_name, location) 
-- VALUES ('Développement', 'Paris');
-- INSERT INTO my_app_departments (department_name, location) 
-- VALUES ('Ressources Humaines', 'Lyon');
-- INSERT INTO my_app_departments (department_name, location) 
-- VALUES ('Marketing', 'Marseille');

-- -- Insertion des employés
-- INSERT INTO my_app_employees (first_name, last_name, email, hire_date, department_id) 
-- VALUES ('John', 'Doe', 'john.doe@example.com', TO_DATE('2021-01-15', 'YYYY-MM-DD'), 1);
-- INSERT INTO my_app_employees (first_name, last_name, email, hire_date, department_id) 
-- VALUES ('Jane', 'Smith', 'jane.smith@example.com', TO_DATE('2022-03-20', 'YYYY-MM-DD'), 2);

-- -- Insertion des projets
-- INSERT INTO my_app_projects (project_name, start_date, end_date, budget)
-- VALUES ('Refonte du site web', TO_DATE('2023-01-01', 'YYYY-MM-DD'), TO_DATE('2023-12-31', 'YYYY-MM-DD'), 50000);
-- INSERT INTO my_app_projects (project_name, start_date, end_date, budget)
-- VALUES ('Lancement d_une nouvelle application mobile', TO_DATE('2024-05-01', 'YYYY-MM-DD'), TO_DATE('2024-12-31', 'YYYY-MM-DD'), 100000);

-- -- Insertion dans la table employee_projects (relation entre employés et projets)
-- INSERT INTO my_app_employee_projects (employee_id, project_id, start_date, end_date)
-- VALUES (1, 1, TO_DATE('2023-01-01', 'YYYY-MM-DD'), TO_DATE('2023-12-31', 'YYYY-MM-DD'));
-- INSERT INTO my_app_employee_projects (employee_id, project_id, start_date, end_date)
-- VALUES (2, 1, TO_DATE('2023-01-01', 'YYYY-MM-DD'), TO_DATE('2023-12-31', 'YYYY-MM-DD'));

-- -- Insertion dans la table salaries
-- INSERT INTO my_app_salaries (employee_id, salary_amount, start_date)
-- VALUES (1, 70000, TO_DATE('2021-01-15', 'YYYY-MM-DD'));
-- INSERT INTO my_app_salaries (employee_id, salary_amount, start_date)
-- VALUES (2, 75000, TO_DATE('2022-03-20', 'YYYY-MM-DD'));

-- -- Insertion des managers des départements
-- INSERT INTO my_app_departments_managers (department_id, manager_id, start_date)
-- VALUES (1, 1, TO_DATE('2021-01-15', 'YYYY-MM-DD'));
-- INSERT INTO my_app_departments_managers (department_id, manager_id, start_date)
-- VALUES (2, 2, TO_DATE('2022-03-20', 'YYYY-MM-DD'));
