import oracledb
import os
from dotenv import load_dotenv

load_dotenv()

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE_PATH = os.getenv("LOG_FILE_PATH", "logs/database_logs.log")

def get_db_config():
    return {
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "dsn": os.getenv("DB_DSN"),
        "mode": oracledb.SYSDBA  # Mode sysdba si nécessaire
    }
