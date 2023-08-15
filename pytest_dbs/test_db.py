import cx_Oracle
import pytest

# Initialize Oracle Client
cx_Oracle.init_oracle_client(lib_dir=r"C:\oib\instantclient_19_9")

# Connect to the Oracle database
@pytest.fixture(scope="module")
def db_connection():
    conn = cx_Oracle.connect(user='apps01', password='apps', dsn='localhost:1521/XE')
    yield conn
    conn.close()

# SELECT operation test
def test_select_operation(db_connection):
    cursor = db_connection.cursor()
    query = "SELECT * FROM test"
    cursor.execute(query)
    result = cursor.fetchall()
    assert len(result) > 0
    cursor.close()

# UPDATE operation test
#def test_update_operation(db_connection):
 #   cursor = db_connection.cursor()
  #  update_query = "UPDATE test SET a = '5' WHERE a=1"
   # cursor.execute(update_query)
    #db_connection.commit()
    
    # Validate the update
    #select_query = "SELECT * FROM test WHERE a = '5'"
    #cursor.execute(select_query)
    #result = cursor.fetchall()
   # assert len(result) > 0
    #cursor.close()

# DELETE operation test
#def test_delete_operation(db_connection):
 #   cursor = db_connection.cursor()
  #  delete_query = "DELETE FROM test WHERE a=5"
  #  cursor.execute(delete_query)
  #  db_connection.commit()
    
    # Validate the delete
   # select_query = "SELECT * FROM test WHERE a=5"
   # cursor.execute(select_query)
   # result = cursor.fetchall()
    #assert len(result) == 0
    #cursor.close()
