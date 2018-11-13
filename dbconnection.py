import sqlite3
import sys

class DBConnection(object):
   db_name = sys.path[0]+"/movie.db"
   def __init__(self):
      self.db_name = self.db_name
   def connection(self):
      conn = sqlite3.connect(self.db_name)
      return conn