import mysql.connector

config = {
  'user': 'zoti',
  'password': 'pass1',
  'host': '127.0.0.1',
  'database': 'broadwaydb',
  'raise_on_warnings': True
}

def get_connection():
    try:
      cnx = mysql.connector.connect(**config)
      return cnx
    except Exception as e:
       print(f"Unable to connect. {e}")
