import cx_Oracle

# Replace these values with your actual Oracle database connection details
#dsn = cx_Oracle.makedsn(host='hostname', port='port', sid='sid_or_service_name')
#username = 'your_username'
#password = 'your_password'
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

        sql_create = """
        CREATE TABLE DB_DETAILS(
            FIRST_NAME VARCHAR2(50),
            LAST_NAME VARCHAR2(50),
            COMPANY VARCHAR2(50),
            AGE NUMBER
        )
         """
        cursor.execute(sql_insert)
    except Exception as err:
        print('Error while inserting the data',err)
    else:
        print('Insert Completed.')
        conn.commit()

finally:
    #cur.closer()
    #conn.close()

# Close the cursor and connection
    cursor.close()
    connection.close()

#create cursor
cursor = conn.cursor()

sql_create = """
CREATE TABLE DB_DETAILS(
    FIRST_NAME VARCHAR2(50),
    LAST_NAME VARCHAR2(50),
    COMPANY VARCHAR2(50),
    AGE NUMBER

)"""

cursor.execute(sql_create)
print('Table Created')


