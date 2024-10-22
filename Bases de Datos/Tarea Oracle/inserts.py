from multiprocessing import connection
import cx_Oracle
import csv

from debugpy import connect

con = cx_Oracle.connect("JUANIN", "42069", "localhost:1521")

print("Database version: ", con.version)

cur = con.cursor()

cur.execute(
    '''
        DROP VIEW v_sales_name
    '''
)
cur.execute(
    '''
        DROP TABLE Tienda
    '''
)
cur.execute(
    '''
        DROP TABLE Biblioteca
    '''
)
cur.execute(
    '''
        DROP SEQUENCE seq_game_id
    '''
)


#rows = cur.fetchall()
#for row in rows:
    #print(row)
con.commit()
cur.close()
con.close()