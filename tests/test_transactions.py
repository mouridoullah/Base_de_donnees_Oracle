import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from unittest.mock import MagicMock
from database_interaction.transactions import manage_transaction

class TestManageTransaction(unittest.TestCase):
    def setUp(self):
        self.connection = MagicMock()
        self.cursor = self.connection.cursor.return_value

    def test_manage_transaction_success(self):
        query = "SELECT * FROM my_app_departments"
        self.cursor.fetchall.return_value = [(1, 'Développement', 'Paris')]

        manage_transaction(self.connection, query)

        self.connection.commit.assert_called_once()
        self.cursor.close.assert_called_once()

    # def test_manage_transaction_failure(self):
    #     query = "SELECT * FROM my_app_departments"
    #     self.cursor.execute.side_effect = Exception("Database error")

    #     try:
    #         manage_transaction(self.connection, query)
    #     except Exception:
    #         pass

    #     self.connection.rollback.assert_called_once()
    #     self.cursor.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()
