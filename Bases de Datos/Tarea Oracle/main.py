from multiprocessing import connection
import cx_Oracle
import csv

from debugpy import connect

con = cx_Oracle.connect("JUANIN", "42069", "localhost:1521")

print("Database version: ", con.version)

'''
Recibe como parametro (cur) que es el cursor que ejecuta los querys
Primero se verifica que existan registros en la tabla biblioteca, si existen se seleccionan todos y se muestran por consola
en caso contrario se muestra un mensaje diciendo que no hay registros
'''
def mostrar_biblioteca(cur):
    cur.execute(
            '''
                SELECT * FROM Biblioteca
            '''
        )
    rows = cur.fetchall()
    if len(rows) == 0:
        print("No hay juegos en biblioteca")
    else:
        for row in rows:
            print(row)

'''
Recibe como parametro (cur) que es el cursor que ejecuta los querys
Primero se pide el nombre y la consola del juego que se quiere comprar, se verifica que no este en biblioteca y se pide el rating que 
se quiere dar al juego, por ultimo se agrega a biblioteca
'''
def comprar_juego(cur):
    n_game = input("Inserte el nombre del juego que quiere comprar: ")
    consola = input('Inserte la consola para la cual quiere comprar el juego: ')
    cur.execute(
            '''
                SELECT * FROM Biblioteca WHERE Name = :name AND Platform = :plat
            ''',
            {'name': n_game, 'plat': consola}
            )
    row = cur.fetchall()
    if len(row) != 0:
        print("No puedes comprar un juego que ya posees")
    else:
        calificacion = int(input("Ingrese rating del juego: "))
        cur.execute(
            '''
                SELECT * FROM Tienda WHERE Name = :name AND Platform = :plat
            ''',
            {'name': n_game, 'plat': consola}
            )
        row = cur.fetchall()
        rank,name,platform,year,genre,publisher,_,_,_,_,_ = row[0]
        cur.execute(
            '''
                INSERT INTO Biblioteca (rank,name,platform,year,genre,publisher,Rating)
                VALUES
                (:1,:2,:3,:4,:5,:6,:7)
            ''',
            (rank,name,platform,year,genre,publisher,calificacion)
            )

'''
Recibe como parametro (cur) que es el cursor que ejecuta los querys
Se selecciona los 5 primeros registros de una tabla tienda ordenada por rank y se muestran por pantalla
'''
def top5_rank(cur):
    cur.execute(
        '''
            SELECT * FROM 
            (SELECT * FROM Tienda ORDER BY Rank)
            WHERE Rank <= 5
        '''
    )
    row = cur.fetchall()
    row.sort()
    for i in row:
        print(i)

'''
Recibe como parametro (cur) que es el cursor que ejecuta los querys
Se pide el genero de los juegos a mostrar y, de una tabla tienda ordenada por rank, se muestran los primeros 5 registros
'''
def top5_genre(cur):
    genero = input("Ingrese genero: ")
    cur.execute(
        '''
            SELECT * FROM
            (SELECT * FROM Tienda ORDER BY Rank)
            WHERE Genre = :genre
            AND ROWNUM <= 5
            
        ''',
        {'genre':genero}
        )
    row = cur.fetchall()
    row.sort()
    for i in row:
        print(i)

'''
Recibe como parametro (cur) que es el cursor que ejecuta los querys
Se pide el nombre del juego a borrar y se verifica que exista en biblioteca
si existe se borra, en caso contrario se muestra por pantalla un mensaje diciendo que no existe
'''
def eliminar_juego(cur):
    nombre = input("Nombre del Juego: ")
    cur.execute(
        '''
            SELECT * FROM Biblioteca
            WHERE Name = :name 
        ''',
        {'name':nombre}
    )
    rows = cur.fetchall()
    if len(rows) == 0:
        print("No puedes borrar un juego que no tienes")
    else:
        cur.execute(
            '''
                DELETE FROM Biblioteca
                WHERE Name = :name
            ''',
            {'name':nombre}
        )

'''
Recibe como parametro (cur) que es el cursor que ejecuta los querys
Primero se pide el nombre del juego, luego se verifica que el juego exista en biblioteca
y por ultimo se pide el nuevo rating y se actualiza
'''
def actualizar_rating(cur):
    nombre = input("Nombre del Juego: ")
    cur.execute(
        '''
            SELECT * FROM Biblioteca
            WHERE Name = :name 
        ''',
        {'name':nombre}
    )
    rows = cur.fetchall()
    if len(rows) == 0:
        print("No puedes actualizar un juego que no tienes")
    else:
        cur.execute(
            '''
                SELECT Rating FROM Biblioteca
                WHERE Name = :name
            ''',
            {'name':nombre}
        )

        rows = cur.fetchall()

        for row in rows:
            print("Rating actual del juego: ",row[0])

        nuevo_rating = int(input("Ingrese nuevo rating: "))

        cur.execute(
            '''
                UPDATE Biblioteca
                SET Rating = :ranting
                WHERE Name = :name
            ''',
            {'ranting':nuevo_rating, 'name': nombre}
        )

'''
Recibe como parametro (cur) que es el cursor que ejecuta los querys
Primero se pide el nombre de la tabla y del juego, luego se busca en la tabla correspondiente y 
se muestra por consola
'''
def buscar_juego(cur):
    tabla = input("Inserte nombre de la tabla donde desea buscar el juego: ")
    nombre = input("Inserte nombre del juego: ")
    if tabla.lower() == 'tienda':
        cur.execute(
            '''
                SELECT * FROM Tienda 
                WHERE Name = :name
            ''',
            {'name':nombre}
        )
    else:
        cur.execute(
            '''
                SELECT * FROM Biblioteca 
                WHERE Name = :name
            ''',
            {'name':nombre}
        )
    rows = cur.fetchall()
    if len(rows) == 0:
        print("No se encontro el juego")
    else:
        for row in rows:
            print(row)

'''
Recibe como parametro (cur) que es el cursor que ejecuta los querys
Primero se pide el nombre de la consola y despues de verifica que exista en la tienda,
si existe se pide la cantidad de lineas que se quiere mostrar y se seleccionan esa cantidad de registros
aleatorios de la tienda y se muestran por pantalla
'''         
def buscar_plataforma(cur):
    nombre = input("Nombre de la consola: ")
    cur.execute(
        '''
            SELECT * FROM Tienda
            WHERE Platform = :name 
        ''',
        {'name':nombre}
    )
    rows = cur.fetchall()
    if len(rows) == 0:
        print("Esta consola no existe en la tienda")
    else:
        lineas = int(input("Numero de juegos que desea mostrar: "))
        cur.execute(
            '''
                SELECT * FROM
                (SELECT * FROM Tienda ORDER BY DBMS_RANDOM.RANDOM)
                    WHERE Platform = :plat
                    AND ROWNUM <= :num
            ''',
            {'plat':nombre, 'num':lineas}
            )
        rows = cur.fetchall()
        for row in rows:
            print(row)

'''
Recibe como parametro (cur) que es el cursor que ejecuta los querys
Primero se verifica que existan juegos para borrar, si existen se muestra por pantalla los nombres de los juegos
que se van a borrar y se pide confirmacion del borrado,
si se confirma se borran todos los juegos, de lo contrario se deja la biblioteca sin alterar
'''
def eliminar_biblioteca(cur):
    cur.execute(
        '''
            SELECT * FROM Biblioteca
        '''
    )
    rows = cur.fetchall()

    if len(rows) == 0:
        print("No tienes juegos para borrar")
    else:
        cur.execute(
            '''
                SELECT * FROM v_sales_name
            '''
        )
        rows = cur.fetchall()
        for row in rows:
            print(row)
        answer = input("Estos son los juegos que vas a eliminar, ¿Estas seguro que quieres eliminar biblioteca?: ")
        if answer.lower() == "si":
            cur.execute(
            '''
                DELETE FROM Biblioteca
            '''
    )

cur = con.cursor()

#Crear tablas
try:
    cur.execute( #create tienda
    '''
        CREATE TABLE Tienda
        (
            Rank INTEGER,
            Name VARCHAR(150),
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

    for e in range(len(year_l)): #Se cambia el valor N/A de algunos juegos para poder ser insertados a la tabla 
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
            CREATE OR REPLACE VIEW v_sales_name
            as SELECT Name
            FROM Biblioteca
        '''
    )
except:
    print("El view ya esta creado")


#Main 


continuar = True
while continuar:
    print(
        '''
            1. Mostrar mi Biblioteca 
            2. Comprar Juego
            3. Mostrar Top 5 Juegos con mayor ranking de ventas totales
            4. Mostrar los 5 juegos mas vendidos segun genero
            5. Eliminar Juego
            6. Actualizar Calificacion
            7. Buscar Juego por Nombre
            8. Buscar juego segun plataforma en Tienda
            9. Eliminar todos los juegos de Biblioteca
            10. Terminar el programa
        '''
        )
    opcion = int(input("Ingresar opcion: "))

    if opcion == 1:
        mostrar_biblioteca(cur)

    elif opcion == 2:
        comprar_juego(cur)

    elif opcion == 3:
        top5_rank(cur)

    elif opcion == 4:
        top5_genre(cur)

    elif opcion == 5:
        eliminar_juego(cur)

    elif opcion == 6:
        actualizar_rating(cur) 
    
    elif opcion == 7:
        buscar_juego(cur)
    
    elif opcion == 8:
        buscar_plataforma(cur)

    elif opcion == 9:
        eliminar_biblioteca(cur)

    else:
        continuar = False
        print("Termino del programa")


con.commit()
cur.close()
con.close()