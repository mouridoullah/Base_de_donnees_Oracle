import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from unittest.mock import patch, MagicMock
from database_interaction.execute import execute_query
from database_interaction.queries import queries

class TestExecuteQuery(unittest.TestCase):
    @patch('database_interaction.execute.get_db_config')
    @patch('database_interaction.execute.oracledb.connect')
    def test_execute_query(self, mock_connect, mock_get_db_config):
        mock_connection = MagicMock()
        mock_connect.return_value = mock_connection

        mock_get_db_config.return_value = {
            "user": "fake_user",
            "password": "fake_password",
            "dsn": "fake_dsn",
            "mode": "SYSDBA"
        }

        execute_query(queries["select_departments"])

        mock_connect.assert_called_once()
        mock_connection.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()
