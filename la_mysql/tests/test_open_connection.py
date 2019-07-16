"""
Test MYSQL Connectivity.
"""

import unittest
import logging
import logging.config
import configparser
from db import connection, housekeeping

logging.config.fileConfig("logging.properties")
logger = logging.getLogger()

class TestMySqlConnection(unittest.TestCase):
    """
    Tests for MySQL connectivity.
    """
    v = 3

    def test_open(self):
      """
      Verify twe can open a database connection with a properties file.
      """
      self.cnx = connection.open()
      logger.info("Test MySQL Connection")
      self.assertIsNotNone(self.cnx)
      self.assertTrue(1==1)
      print("Connected ....")
      self.cnx.close()
 
    def test_open_with(self):
      """
      Verify we can open a database connection with parameters.
      """
      config = configparser.RawConfigParser()
      config.read("config.properties")

      user = config.get('DatabaseSection','mysql.user') 
      password = config.get('DatabaseSection','mysql.password')
      host = config.get('DatabaseSection','mysql.host')
      port = config.get('DatabaseSection','mysql.port')
      database = config.get('DatabaseSection','mysql.database')

      self.cnx = connection.openWith(user=user, password=password, host=host, port=port, database=database)
      logger.info("Test MySQL Connection")
      self.assertIsNotNone(self.cnx)
      self.assertTrue(1==1)
      print("Connected ....")
      self.cnx.close()

    def test_truncate(self):
      housekeeping.truncate(connection.open(), "explore.topics")
 
    def test_insert_by_parameters(self):
      cnx = connection.open()
      housekeeping.truncate(cnx, "explore.topics")
      insertSQL = self.makesql(1, "physics", "science and that")
      housekeeping.insert(cnx, insertSQL)
      insertSQL = self.makesql(2, "biology", "animals and that")
      housekeeping.insert(cnx, insertSQL)
      insertSQL = self.makesql(3, "maths", "hilter and that")
      housekeeping.insert(cnx, insertSQL)
      cnx.close()

    def makesql(self, id, subject, desc):
      sql = f"insert into topics (ID, subject, description) values ({id}, '{subject}', '{desc}')"
      print("SQL:", sql)
      return sql

if __name__ == '__main__':
    unittest.main()
