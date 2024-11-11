import logging
import oracledb

def manage_transaction(connection, query):
    try:
        cursor = connection.cursor()
        logging.info(f"Début de l'exécution de la requête : {query}")
        cursor.execute(query)

        results = cursor.fetchall()
        for row in results:
            logging.debug(f"Résultat : {row}")

        logging.info("Requête exécutée avec succès.")
        connection.commit()
        cursor.close()
    except oracledb.DatabaseError as e:
        connection.rollback()  # Rollback en cas d'erreur
        error_msg = f"Erreur lors de l'exécution de la requête : {e}"
        logging.error(error_msg)
