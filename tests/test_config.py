import sys
import oracledb
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from config.db_config import get_db_config

class TestDBConfig(unittest.TestCase):
    def test_get_db_config(self):
        config = get_db_config()
        self.assertIn("user", config)
        self.assertIn("password", config)
        self.assertIn("dsn", config)
        self.assertEqual(config["mode"], oracledb.SYSDBA)

if __name__ == '__main__':
    unittest.main()
