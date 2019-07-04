"""
Test MYSQL Connectivity.
"""

import unittest
import logging
import logging.config
from db import connection

logging.config.fileConfig("logging.properties")
logger = logging.getLogger()

class TestMySqlConnection(unittest.TestCase):
    """
    Tests for MySQL connectivity.
    """

    def test_open(self):
      """
      Verify that all implementations have same result.
      """
      cnx = connection.open();
      logger.info("Test MySQL Connection")
      self.assertIsNotNone(cnx)
      self.assertTrue(1==1);


if __name__ == '__main__':
    unittest.main()
