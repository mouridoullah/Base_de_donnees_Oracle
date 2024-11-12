import oracledb
import os
from dotenv import load_dotenv

load_dotenv()

def get_db_config():
    return {
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "dsn": os.getenv("DB_DSN"),
        "mode": oracledb.SYSDBA  # Mode sysdba si nécessaire
    }
