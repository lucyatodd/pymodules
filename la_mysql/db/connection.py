from mysql.connector import (connection)
import configparser
import io

def open():
   config = configparser.RawConfigParser()
   config.read("config.properties")

   user = config.get('DatabaseSection','mysql.user') 
   password = config.get('DatabaseSection','mysql.password')
   host = config.get('DatabaseSection','mysql.host')
   port = config.get('DatabaseSection','mysql.port')
   database = config.get('DatabaseSection','mysql.database')

   details = f"{user} {password} {host} {port} {database}"
   print("details ", details)

   cnx = connection.MySQLConnection(user=user, password=password, host=host, port=port, database=database)
   return cnx

def openWith(user, password, host, port, database):
   details = f"{user} {password} {host} {port} {database}"
   print("details ", details)
   cnx = connection.MySQLConnection(user=user, password=password, host=host, port=port, database=database)
   return cnx
