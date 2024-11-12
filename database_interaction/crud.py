from database_interaction.execute import execute_query
import logging

def create_entry(query, params):
    logging.info("Création d'une nouvelle entrée...")
    execute_query(query, params)

def read_entries(query, params=None):
    logging.info("Lecture des entrées...")
    return execute_query(query, params, fetch=True)

def update_entry(query, params):
    logging.info("Mise à jour d'une entrée...")
    execute_query(query, params)

def delete_entry(query, params):
    logging.info("Suppression d'une entrée...")
    execute_query(query, params)
