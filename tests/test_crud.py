import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from unittest.mock import patch, MagicMock
from database_interaction.crud import create_entry, read_entries, update_entry, delete_entry

class TestCRUDOperations(unittest.TestCase):

    @patch('database_interaction.crud.get_db_config')
    @patch('database_interaction.crud.oracledb.connect')
    def test_create_entry(self, mock_connect, mock_get_db_config):
        mock_connection = MagicMock()
        mock_connect.return_value = mock_connection

        create_entry("INSERT INTO my_app_departments (department_name, location) VALUES (:1, :2)", ("Informatique", "Paris"))

        mock_connect.assert_called_once()
        mock_connection.commit.assert_called_once()
        mock_connection.close.assert_called_once()

    @patch('database_interaction.crud.get_db_config')
    @patch('database_interaction.crud.oracledb.connect')
    def test_read_entries(self, mock_connect, mock_get_db_config):
        mock_connection = MagicMock()
        mock_connect.return_value = mock_connection
        mock_connection.cursor.return_value.fetchall.return_value = [("Informatique", "Paris")]

        results = read_entries("SELECT * FROM my_app_departments")

        mock_connect.assert_called_once()
        self.assertEqual(results, [("Informatique", "Paris")])
        mock_connection.close.assert_called_once()

    @patch('database_interaction.crud.get_db_config')
    @patch('database_interaction.crud.oracledb.connect')
    def test_update_entry(self, mock_connect, mock_get_db_config):
        mock_connection = MagicMock()
        mock_connect.return_value = mock_connection

        update_entry("UPDATE my_app_departments SET location = :1 WHERE department_name = :2", ("Londres", "Informatique"))

        mock_connect.assert_called_once()
        mock_connection.commit.assert_called_once()
        mock_connection.close.assert_called_once()

    @patch('database_interaction.crud.get_db_config')
    @patch('database_interaction.crud.oracledb.connect')
    def test_delete_entry(self, mock_connect, mock_get_db_config):
        mock_connection = MagicMock()
        mock_connect.return_value = mock_connection

        delete_entry("DELETE FROM my_app_departments WHERE department_name = :1", ("Informatique",))

        mock_connect.assert_called_once()
        mock_connection.commit.assert_called_once()
        mock_connection.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()
