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
    #create table
    #cur=conn.cursor()
    #cursor.execute('''CREATE TABLE CodeSpeedy(employee_id number(10),employee_name varchar2(10))''')
    #print("Table Created")
    query1 = cursor.execute('''INSERT INTO CodeSpeedy values(101,'Ravi')''') 
    cursor.execute(query1)
    query2 = cursor.execute('''INSERT INTO CodeSpeedy values(102,'Ramu')''')
    cursor.execute(query2)
    query3 = cursor.execute('''INSERT INTO CodeSpeedy values(103,'Rafi')''')
    cursor.execute(query3)
    conn.commit()
    print("***")
    #update_query = "UPDATE CodeSpeedy SET employee_name = 'David' WHERE employee_name = 'John';"
    #cursor.execute(update_query)
    # Fetch and print results
    #for row in cursor:
     #   print(row)

except cx_Oracle.Error as error:
    print("Database error:", error)
finally:
    # Close cursor and connection
  ##  cursor.close()
    conn.close()
