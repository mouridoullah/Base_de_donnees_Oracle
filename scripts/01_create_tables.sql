-- Création de l'utilisateur
CREATE USER my_app_user IDENTIFIED BY monMotDePasse;
GRANT CONNECT, RESOURCE TO my_app_user;

-- Création de la table des départements
CREATE TABLE my_app_departments (
    department_id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    department_name VARCHAR2(100) NOT NULL,
    location VARCHAR2(100)
);

-- Ajout d'un index sur le nom des départements
CREATE INDEX idx_department_name ON my_app_departments (department_name);

-- Création de la table des employés
CREATE TABLE my_app_employees (
    employee_id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    first_name VARCHAR2(50),
    last_name VARCHAR2(50),
    email VARCHAR2(100) UNIQUE,
    hire_date DATE DEFAULT SYSDATE,
    department_id NUMBER,
    FOREIGN KEY (department_id) REFERENCES my_app_departments(department_id)
);

-- Ajout d'un index sur le nom de famille des employés
CREATE INDEX idx_employee_last_name ON my_app_employees (last_name);

-- Création de la table des projets
CREATE TABLE my_app_projects (
    project_id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    project_name VARCHAR2(100),
    start_date DATE,
    end_date DATE,
    budget NUMBER
);

-- Ajout d'un index sur le nom des projets
CREATE INDEX idx_project_name ON my_app_projects (project_name);

-- Table pour associer les employés aux projets (relation N:M)
CREATE TABLE my_app_employee_projects (
    employee_id NUMBER,
    project_id NUMBER,
    start_date DATE DEFAULT SYSDATE,
    end_date DATE,
    PRIMARY KEY (employee_id, project_id),
    FOREIGN KEY (employee_id) REFERENCES my_app_employees(employee_id),
    FOREIGN KEY (project_id) REFERENCES my_app_projects(project_id)
);

-- Table des salaires
CREATE TABLE my_app_salaries (
    salary_id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    employee_id NUMBER,
    salary_amount NUMBER,
    start_date DATE,
    end_date DATE,
    FOREIGN KEY (employee_id) REFERENCES my_app_employees(employee_id)
);

-- Ajout d'un index sur le montant des salaires
CREATE INDEX idx_salary_amount ON my_app_salaries (salary_amount);

-- Création d'une table pour les managers de département
CREATE TABLE my_app_departments_managers (
    department_id NUMBER,
    manager_id NUMBER,
    start_date DATE DEFAULT SYSDATE,
    PRIMARY KEY (department_id),
    FOREIGN KEY (department_id) REFERENCES my_app_departments(department_id),
    FOREIGN KEY (manager_id) REFERENCES my_app_employees(employee_id)
);

-- Ajout d'un index sur l'ID du manager
CREATE INDEX idx_manager_id ON my_app_departments_managers (manager_id);
