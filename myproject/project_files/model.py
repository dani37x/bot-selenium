import mysql.connector

class Operations():
  def __init__(self, config):
    self.connection = mysql.connector.connect(**config)

  def query(self, sql, args):
    cursor = self.connection.cursor()
    cursor.execute(sql, args)
    return cursor

  def insert(self, sql, args):
    cursor = self.query(sql, args)
    id = cursor.lastrowid
    self.connection.commit()
    cursor.close()
    return id
 
  def close(self):
      self.connection.close()


    