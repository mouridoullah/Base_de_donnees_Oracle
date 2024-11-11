import logging
import oracledb
from database_interaction.config import get_db_config
from database_interaction.manage_transaction import manage_transaction

def execute_query(query):
    connection = None
    try:
        db_config = get_db_config()
        logging.info("Connexion à la base de données...")
        connection = oracledb.connect(**db_config)
        manage_transaction(connection, query)
    finally:
        if connection:
            connection.close()
            logging.info("Connexion à la base de données fermée.")
