#! /usr/bin/env python

import connection
# crea tables del sistema
def createTables():
    
    conn = connection.connection()
    cur = conn.cursor()

    # users table
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        id serial PRIMARY KEY,
        username varchar(50) NOT NULL,
        email varchar(50) NOT NULL,
        password varchar(50) NOT NULL,
        is_tutor boolean NOT NULL);
        """)

    cur.execute("""CREATE TABLE IF NOT EXISTS memorice (
        id serial PRIMARY KEY,
        Nota varchar(50) NOT NULL,
        primera varchar(250) NOT NULL,
        segunda varchar(250) NOT NULL);
        """)
    
    cur.execute("""CREATE TABLE IF NOT EXISTS tempos (
        id serial PRIMARY KEY,
        tempo varchar(50) NOT NULL,
        imagen varchar(250) NOT NULL,
        audio varchar(250) NOT NULL);
        """)
    
    cur.execute("""CREATE TABLE IF NOT EXISTS resumenes (
        id serial PRIMARY KEY,
        actividad varchar(50) NOT NULL,
        aciertos varchar(50) NOT NULL,
        fallos varchar(50) NOT NULL,
        fecha varchar(50) NOT NULL);
        """)
    
    cur.execute("""CREATE TABLE IF NOT EXISTS emparejar (
        id serial PRIMARY KEY,
        actividad varchar(50) NOT NULL,
        imagen varchar(50) NOT NULL,
        audio varchar(50) NOT NULL,
        tipo varchar(50) NOT NULL);
        """)

    conn.commit()
    print("All tables created successfully")

createTables()
