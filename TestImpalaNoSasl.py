from impala.dbapi import connect
import traceback 
try:
    conn   = connect(host = '10.10.100.53', port = 21050)
    cursor = conn.cursor()
    #sql      = "select * from cdnportal.monitor"
    sql      = "show databases;"
    cursor.execute(sql)
    print cursor.fetchall()
except:
    traceback.print_exc()
