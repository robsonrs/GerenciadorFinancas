import mysql.connector

config = {
  'user': 'admin',
  'password': 'abc1234',
  'host': '127.0.0.1',
  'database': 'gerenciadorfinancas',
  'raise_on_warnings': True
}

def open_connection():
    return mysql.connector.connect(**config)