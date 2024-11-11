import sys
import os

# Ajouter le répertoire parent au chemin de recherche des modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database_interaction.execute import execute_query
import unittest
from unittest.mock import patch, MagicMock

class TestExecuteQuery(unittest.TestCase):
    @patch("database_interaction.execute.oracledb.connect")
    def test_execute_query_success(self, mock_connect):
        mock_conn = MagicMock()
        mock_connect.return_value = mock_conn
        mock_cursor = mock_conn.cursor.return_value
        mock_cursor.fetchall.return_value = [("IT",), ("HR",)]

        # Appel de la fonction à tester
        execute_query("SELECT * FROM my_app_departments")

        # Vérifiez que la requête a été exécutée et les résultats affichés
        mock_cursor.execute.assert_called_once_with("SELECT * FROM my_app_departments")
        mock_cursor.fetchall.assert_called_once()
        mock_cursor.close.assert_called_once()
        mock_conn.close.assert_called_once()

    @patch("database_interaction.execute.oracledb.connect")
    def test_execute_query_failure(self, mock_connect):
        mock_conn = MagicMock()
        mock_connect.return_value = mock_conn
        mock_cursor = mock_conn.cursor.return_value
        mock_cursor.execute.side_effect = Exception("Database error")

        # Appel de la fonction à tester
        with self.assertRaises(Exception) as context:
            execute_query("SELECT * FROM my_app_departments")

        self.assertIn("Database error", str(context.exception))

if __name__ == '__main__':
    unittest.main()
