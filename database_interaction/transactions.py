import logging
import time
import oracledb

def manage_transaction(connection, query, params=None, fetch=False):
    start_time = time.time()
    cursor = None
    try:
        cursor = connection.cursor()
        logging.info(f"Exécution de la requête : {query}")
        cursor.execute(query, params or {})

        if fetch:
            results = cursor.fetchall()
            execution_time = time.time() - start_time
            logging.info(f"Requête exécutée en {execution_time:.2f} secondes avec résultats.")
            return results
        else:
            connection.commit()
            execution_time = time.time() - start_time
            logging.info(f"Requête exécutée en {execution_time:.2f} secondes sans résultats.")
    except oracledb.DatabaseError as e:
        if connection:
            connection.rollback()
        logging.error(f"Erreur lors de l'exécution de la requête : {e}")
    finally:
        if cursor:
            cursor.close()
