import logging
import os

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE_PATH = os.getenv("LOG_FILE_PATH", "logs/database_logs.log")

def setup_logger():
    logging.basicConfig(
        filename=LOG_FILE_PATH,
        level=getattr(logging, LOG_LEVEL.upper(), logging.INFO),  # Utilise le niveau de log de l'env
        format="%(asctime)s - %(levelname)s - %(module)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    # Console handler pour afficher les logs dans la console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(getattr(logging, LOG_LEVEL.upper(), logging.INFO))
    console_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logging.getLogger().addHandler(console_handler)
    