import logging
import logging.config

logging.config.fileConfig("logging.properties")
logger = logging.getLogger()

def insert(cnx, sql):  
   cursor = cnx.cursor()
   logger.info("Executing: %s", sql)
   cursor.execute(sql)
   logger.info("Exectued")
   cursor.execute("commit")

def truncate(cnx, tablename):
   logger.info("Truncating %s", tablename)
   sql = f"truncate {tablename}"
   cursor = cnx.cursor()
   cursor.execute(sql)