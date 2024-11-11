import sys
import os
import unittest
from unittest.mock import MagicMock, patch

# Ajouter le répertoire parent au chemin de recherche des modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database_interaction.manage_transaction import manage_transaction

class TestManageTransaction(unittest.TestCase):
    @patch('database_interaction.manage_transaction.oracledb.connect')
    def test_manage_transaction_success(self, mock_connect):
        mock_conn = MagicMock()
        mock_connect.return_value = mock_conn
        mock_cursor = mock_conn.cursor.return_value
        mock_cursor.fetchall.return_value = [("Project X", "John Doe")]

        # Appel de la fonction à tester
        manage_transaction(mock_conn, "SELECT * FROM my_app_projects")

        # Vérifiez que la requête a été exécutée et les résultats affichés
        mock_cursor.execute.assert_called_once_with("SELECT * FROM my_app_projects")
        mock_cursor.fetchall.assert_called_once()
        mock_cursor.close.assert_called_once()
        mock_conn.commit.assert_called_once()
        mock_conn.close.assert_called_once()

    @patch('database_interaction.manage_transaction.oracledb.connect')
    def test_manage_transaction_failure(self, mock_connect):
        mock_conn = MagicMock()
        mock_connect.return_value = mock_conn
        mock_cursor = mock_conn.cursor.return_value
        mock_cursor.execute.side_effect = Exception("Query execution failed")

        # Appel de la fonction à tester
        with self.assertRaises(Exception) as context:
            manage_transaction(mock_conn, "SELECT * FROM my_app_projects")

        self.assertIn("Query execution failed", str(context.exception))
        mock_conn.rollback.assert_called_once()
        mock_cursor.close.assert_called_once()
        mock_conn.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()
