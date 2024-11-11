import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database_interaction.config import get_db_config
import unittest

class TestConfig(unittest.TestCase):
    def test_get_db_config(self):
        config = get_db_config()
        self.assertIn('user', config)
        self.assertIn('password', config)
        self.assertIn('dsn', config)

if __name__ == '__main__':
    unittest.main()
