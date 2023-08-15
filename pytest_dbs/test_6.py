import cx_Oracle

# Declare cursor variable
cursor = None
conn= None
try:
    # Connect to the Oracle database
    conn = cx_Oracle.connect('apps01/apps@//localhost:1521/XEPDB1')
    print(conn.version)
    
    try:
        # Create a cursor
        cursor = conn.cursor()
        
        # SQL insert statement with placeholders
        sql_insert = """INSERT INTO DB_DETAILS VALUES (:1, :2, :3, :4)"""
        
        # Execute the insert statement
        data = [('Bill', 'Gates', 'Microsoft', 67),('Mark','Zuck','Facebook',35)]
        cursor.execute(sql_insert, data)
        
        # Commit the transaction
        conn.commit()
        print('Insert Completed.')
        
    except Exception as err_insert:
        print('Error while inserting the data', err_insert)
        conn.rollback()  # Rollback the transaction in case of an error
    
finally:
    if cursor is not None:
        cursor.close()  # Close the cursor
    if conn is not None:
        conn.close()  # Close the connection
