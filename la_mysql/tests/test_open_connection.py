"""
Test MYSQL Connectivity.
"""

import unittest
import logging
import logging.config
import configparser
from db import connection

logging.config.fileConfig("logging.properties")
logger = logging.getLogger()

class TestMySqlConnection(unittest.TestCase):
    """
    Tests for MySQL connectivity.
    """

    def test_open(self):
      """
      Verify twe can open a database connection with a properties file.
      """
      self.cnx = connection.open();
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

      self.cnx = connection.openWith(user=user, password=password, host=host, port=port, database=database);
      logger.info("Test MySQL Connection")
      self.assertIsNotNone(self.cnx)
      self.assertTrue(1==1)
      print("Connected ....")
      self.cnx.close()
 
    def test_insert(self):  
      self.cnx = connection.open();
      mycursor = self.cnx.cursor()
      self.insert(mycursor, 70)
      print("Insert exectued")
      self.cnx.close()

    def makesql(self, id, subject, desc):
      sql = f"insert into topics (ID, subject, description) values ({id}, '{subject}', '{desc}')"
      print("SQL:", sql)
      return sql

    # execute the 3 insert commands with different parameters
    def insert(self, cursor, id):
      cursor.execute(self.makesql(id+1, "physics", "science and that"))
      cursor.execute(self.makesql(id+2, "biology", "animals and that"))
      cursor.execute(self.makesql(id+3, "german", "hilter and that"))
      cursor.execute("commit")

if __name__ == '__main__':
    unittest.main()
