from multiprocessing import connection
import cx_Oracle
import csv

from debugpy import connect

con = cx_Oracle.connect("JUANIN", "42069", "localhost:1521")

print("Database version: ", con.version)

cur = con.cursor()

nombre = "Wii"

cur.execute( #create view
        '''
            CREATE OR REPLACE VIEW v_sales_name
            as SELECT Name
            FROM Biblioteca
        '''
    )






con.commit()
cur.close()
con.close()