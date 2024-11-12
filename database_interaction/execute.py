from config.db_config import get_db_config
from database_interaction.transactions import manage_transaction
import logging
import oracledb

def execute_query(query, params=None, fetch=False):
    connection = None
    try:
        db_config = get_db_config()
        logging.info("Connexion à la base de données...")
        connection = oracledb.connect(**db_config)
        return manage_transaction(connection, query, params, fetch)
    except oracledb.DatabaseError as e:
        logging.error(f"Erreur dans execute_query : {e}")
    finally:
        if connection:
            connection.close()
            logging.info("Connexion à la base de données fermée.")
