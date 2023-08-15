import cx_Oracle


conn=None
cursor=None

try:
# Connect to the Oracle database
    conn = cx_Oracle.connect('apps01/apps@//localhost:1521/XEPDB1')
except Exception as err:
    print('Error while creating the connection', err)
else:    
    print(conn.version)
    try:
        #create cursor
        cursor = conn.cursor()
        sql_insert = """INSERT INTO DB_DETAILS VALUES ('Lily','Jobs','Apple',56)"""
        cursor.execute(sql_insert)
    except Exception as err:
        print('Error while inserting the data', err)
    else:
        print('Insert Completed.')
        conn.commit()

finally:
    cursor.close()
    conn.close()