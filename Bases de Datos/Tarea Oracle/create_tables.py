from multiprocessing import connection
import cx_Oracle
import csv

from debugpy import connect

con = cx_Oracle.connect("JUANIN", "42069", "localhost:1521")

print("Database version: ", con.version)

cur = con.cursor()

try:
    cur.execute( #create tienda
    '''
        CREATE TABLE Tienda
        (
            Rank INTEGER,
            Name VARCHAR(50),
            Platform VARCHAR(50),
            Year INTEGER,
            Genre VARCHAR(50),
            Publisher VARCHAR(50),
            NA_Sales FLOAT,
            EU_Sales FLOAT,
            JP_Sales FLOAT,
            Other_Sales FLOAT,
            Global_Sales FLOAT
        )
        
    '''
    )
    excel = []

    with open('juegos.csv') as f:
        reader = csv.reader(f)
        for rank,name,platform,year,genre,publisher,na_sales,eu_sales,jp_sales,other_sales,global_sales in reader:
            excel.append((rank,name,platform,year,genre,publisher,na_sales,eu_sales,jp_sales,other_sales,global_sales)) 

    rank_l = []
    name_l = []
    platform_l = []
    year_l = []
    genre_l = []
    publisher_l = []
    na_sales_l = []
    eu_sales_l = []
    jp_sales_l = []
    other_sales_l = []
    global_sales_l = []

    with open('juegos.csv') as f:
        reader = csv.reader(f)
        for rank,name,platform,year,genre,publisher,na_sales,eu_sales,jp_sales,other_sales,global_sales in reader:
            rank_l.append(rank) 
            name_l.append(name) 
            platform_l.append(platform) 
            year_l.append(year) 
            genre_l.append(genre) 
            publisher_l.append(publisher) 
            na_sales_l.append(na_sales) 
            eu_sales_l.append(eu_sales) 
            jp_sales_l.append(jp_sales) 
            other_sales_l.append(other_sales) 
            global_sales_l.append(global_sales) 

    for e in range(len(year_l)):
        if year_l[e] == 'N/A':
            year_l[e] = 0

    excel = []
    i = 1
    while i < len(rank_l):
        tupl = (int(rank_l[i]),name_l[i],platform_l[i],int(year_l[i]),genre_l[i],publisher_l[i],float(na_sales_l[i]),float(eu_sales_l[i]),float(jp_sales_l[i]),float(other_sales_l[i]),float(global_sales_l[i]))
        excel.append(tupl)
        i += 1 

    for rank,name,platform,year,genre,publisher,na_sales,eu_sales,jp_sales,other_sales,global_sales in excel:
        cur.execute(
        '''INSERT INTO Tienda (Rank,Name,Platform,Year,Genre,Publisher,Na_sales,Eu_sales,Jp_sales,Other_sales,Global_sales)
            VALUES 
            (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11)
            ''',
            (int(rank),name,platform,int(year),genre,publisher,float(na_sales),float(eu_sales),float(jp_sales),float(other_sales),float(global_sales))
        )

except:
    print("La tabla tienda ya esta creada")





try:
    cur.execute( #create biblioteca
    '''
        CREATE TABLE Biblioteca
        (
            Id INTEGER NOT NULL,
            Rank INTEGER,
            Name VARCHAR(150),
            Platform VARCHAR(50),
            Year INTEGER,
            Genre VARCHAR(50),
            Publisher VARCHAR(50),
            Rating INTEGER
        )
    '''
)
except:
    print("La tabla biblioteca ya esta creada")

try:
    cur.execute( #create trigger
    '''
        CREATE SEQUENCE seq_game_id
        START WITH 1
        INCREMENT BY 1
        NOCACHE
        NOCYCLE
    '''
    )
    cur.execute( #create or replace trigger
        '''
            CREATE OR REPLACE TRIGGER id_autoincrement
            BEFORE INSERT
            ON Biblioteca
            FOR EACH ROW
            BEGIN
            :new.Id:=seq_game_id.nextval;
            END;
        '''
    )
except:
    print("El trigger ya esta creado")

try:
    cur.execute( #create view
        '''
            CREATE VIEW v_sales_name
            as SELECT Name, Global_sales 
            FROM (SELECT * FROM Tienda ORDER BY Rank)
        '''
    )
except:
    print("El view ya esta creado")