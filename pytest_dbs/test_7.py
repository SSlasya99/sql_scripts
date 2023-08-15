import cx_Oracle
import os

#Set Oracle Client library path (adjust this to your actual installation path)
#os.environ['PATH'] = r'C:\Program Files\Python311\instantclient_21_10'
cx_Oracle.init_oracle_client(lib_dir=r"C:\oib\instantclient_19_9")

conn = cx_Oracle.connect('apps01','apps','localhost:1521/XE')

#connection = cx_Oracle.connect(user="apps01", password='apps',
#                               dsn="localhost/XE",
#                               encoding="UTF-8")
## Create a cursor
cursor = conn.cursor()

try:
    # Establish a connection
    #conn = cx_Oracle.connect('sys/Tiger@//localhost:1521/XEPDB1')
    # Create a cursor
    #cursor = conn.cursor()
    # Execute a query
   # query = "INSERT INTO TEST('ID')VALUES(1);SELECT * FROM test;"
    update_query = "UPDATE test SET a = 5 WHERE a = 1"
    cursor.execute(update_query)
    # Fetch and print results
    for row in cursor:
        print(row)
except cx_Oracle.Error as error:
    print("Database error:", error)
finally:
    # Close cursor and connection
  ##  cursor.close()
    conn.close()