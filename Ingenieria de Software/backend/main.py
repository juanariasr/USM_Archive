#! /usr/bin/env python
from pydantic import BaseModel
from typing import Optional
from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from psycopg2.extras import RealDictCursor
from psycopg2 import sql
import json

import connection
from tables import createTables


# instancia de FastAPI
app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Tempo(BaseModel):
    tempo: str
    imagen: str
    audio: str 

class User(BaseModel):
    username: str
    email: Optional[str]
    password: str
    is_tutor: bool

class Login(BaseModel):
    username: str
    password: str

class Resumen(BaseModel):
    actividad: str
    aciertos: str
    fallos: str
    fecha: str 

class Emparejar(BaseModel):
    actividad: str
    imagen: str
    audio: str
    tipo: str 

class CardMemorice(BaseModel):
    Nota: str
    primera: str
    segunda: str 

class Song(BaseModel):
    username: str
    song: str


createTables()

@app.post("/resumenes")
async def createResumenes(resumen: Resumen):
    conn = connection.connection()
    cur = conn.cursor()
    
    try:
        cur.execute("""INSERT INTO resumenes (actividad, aciertos, fallos, fecha) 
                    VALUES(%s, %s, %s, %s)""", (resumen.actividad, resumen.aciertos, resumen.fallos,
                                                resumen.fecha))
        conn.commit()
        return JSONResponse(content={"message": "Resumen created successfully"},
                            status_code=status.HTTP_201_CREATED)
    except Exception as e:
        print(e)
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@app.post("/users")
async def createUsers(user: User):
    conn = connection.connection()
    cur = conn.cursor()

    try:
        cur.execute("""INSERT INTO users (username, email, password, is_tutor) 
                    VALUES(%s, %s, %s, %s)""", (user.username, user.email,
                                                user.password, user.is_tutor))
        conn.commit()
        return JSONResponse(content={"message": "User created successfully"},
                            status_code=status.HTTP_201_CREATED)
    except Exception as e:
        print(e)
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@app.get("/users/{id}")
async def showUser(id: int):
    conn = connection.connection()
    cur = conn.cursor()

    try:
        cur.execute("""SELECT * FROM users WHERE id = %s""", (id,))
        data = cur.fetchall()
        conn.commit()
        return JSONResponse(content=data,
                            status_code=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@app.get("/users/")
async def showUser(username: str):
    conn = connection.connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    try:
        cur.execute("""SELECT * FROM users WHERE username =
                    '{0}'""".format(username))

        data = cur.fetchall()
        data = json.dumps(data)

        return JSONResponse(content=data,
                            status_code=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return JSONResponse(content={"message": "Error"},
                            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Login users post
@app.post("/users/login")
async def showUser(login: Login):
    conn = connection.connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    username = login.username
    password = login.password

    try:
        query = sql.SQL("""SELECT * FROM users WHERE username =
                        '{0}'""".format(username))
        cur.execute(query)
        result = cur.fetchone()
        if result and result['password'] == password:
            return JSONResponse(content={"message": "Success"},
                                status_code=200)

        elif result and result['password'] != password:
            return JSONResponse(content={"message": "Wrong password"},
                                status_code=401)

        elif len(result) == 0:
            return JSONResponse(content={"message": "Error"},
                                status_code=404)

    except Exception as e:
        print(e)
        return JSONResponse(content={"message": "Error"},
                            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    finally:
        # Close the database connection
        if cur:
            cur.close()
        if conn:
            conn.close()


@app.put("/users/{id}")
async def updateUser(id: int, user: User):
    conn = connection.connection()
    cur = conn.cursor()

    try:
        cur.execute("""UPDATE users SET (username, email, password)
                    WHERE id = %d, VALUES (%s, %s, %s)""", (User.name,
                                                            User.password,
                                                            User.email))
        conn.commit()
        return JSONResponse(content={"message": "User updated successfully"},
                            status_code=status.HTTP_200_OK)

    except Exception as e:
        print(e)
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@app.delete("/users/{id}")
async def deleteUser(id: int):
    conn = connection.connection()
    cur = conn.cursor()

    try:
        cur.execute("""DELETE FROM users WHERE id = %s""", (id,))
        conn.commit()
        return JSONResponse(content={"message": "User delete successfully"},
                            status_code=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return JSONResponse(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR)

@app.post("/memorice")
async def createMemorice(card: CardMemorice):
    conn = connection.connection()
    cur = conn.cursor()

    try:
        cur.execute("""INSERT INTO memorice (Nota, primera, segunda) 
                    VALUES(%s, %s, %s)""", (card.Nota, card.primera,
                                                card.segunda))
        conn.commit()
        return JSONResponse(content={"message": "Card created successfully"},
                            status_code=status.HTTP_201_CREATED)
    except Exception as e:
        print(e)
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

@app.get("/memorice")
async def showMemorice():
    conn = connection.connection()
    cur = conn.cursor()
   
    try:
        cur.execute("""SELECT * FROM memorice""")
        cards = cur.fetchall()
        return JSONResponse(content= cards, status_code=status.HTTP_200_OK)

    except Exception as e:
        print(e)
        return JSONResponse(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@app.put("/memorice/{id}")
async def updateCard(id: int, new_data: CardMemorice):
    conn = connection.connection()
    cur = conn.cursor()

    try:
        cur.execute("UPDATE educador SET Nota = %s, primera = %s, segunda = %s WHERE id = %s", 
                (new_data.Nota, new_data.primera, new_data.segunda, id))
        conn.commit()
        return JSONResponse(content= {"message": "Card updated successfully"},
                            status_code=status.HTTP_200_OK)

    except Exception as e:
        print(e)
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

@app.delete("/memorice/{id}")
async def deleteCard(id: int):
    conn = connection.connection()
    cur = conn.cursor()
   
    try:
        cur.execute("""DELETE FROM memorice WHERE id = %s""", (id,))
        conn.commit()
        return JSONResponse(content = {"message": "Card delete successfully"},
                            status_code = status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return JSONResponse(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR)

@app.post("/tempo")
async def createTempo(tempo: Tempo):
    conn = connection.connection()
    cur = conn.cursor()

    try:
        cur.execute("""INSERT INTO tempos (tempo, imagen, audio) 
                    VALUES(%s, %s, %s)""", (tempo.tempo, tempo.imagen,
                                                tempo.audio))
        conn.commit()
        return JSONResponse(content={"message": "Tempo created successfully"},
                            status_code=status.HTTP_201_CREATED)
    except Exception as e:
        print(e)
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

@app.get("/tempo")
async def showTempo():
    conn = connection.connection()
    cur = conn.cursor()

    try:
        cur.execute("""SELECT * FROM tempos""")
        tempo = cur.fetchall()
        return JSONResponse(content= tempo, status_code=status.HTTP_200_OK)

    except Exception as e:
        print(e)
        return JSONResponse(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR)

@app.put("/tempo/{id}")
async def updateUser(id: int, new_data: User):
    conn = connection.connection()
    cur = conn.cursor()

    try:
        cur.execute("""UPDATE users SET (tempo, imagen, audio)
                    WHERE id = %d, VALUES (%s, %s, %s)""", (Tempo.tempo,
                                                            Tempo.imagen,
                                                            Tempo.audio))
        conn.commit()
        return JSONResponse(content= {"message": "Tempo updated successfully"},
                            status_code=status.HTTP_200_OK)

    except Exception as e:
        print(e)
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

@app.delete("/tempo/{id}")
async def deleteTempo(id: int):
    conn = connection.connection()
    cur = conn.cursor()
   
    try:
        cur.execute("""DELETE FROM tempos WHERE id = %s""", (id,))
        conn.commit()
        return JSONResponse(content = {"message": "Tempo delete successfully"},
                            status_code = status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return JSONResponse(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR)

    finally:
        # Close the database connection
        if cur:
            cur.close()
        if conn:
            conn.close()

#==================TEMPO==============

#===================NOTAS==============
@app.get("/notas/{username}")
async def getSongs(username: str):
    conn = connection.connection()
    cur = conn.cursor()
    cur.execute("""SELECT * FROM songs WHERE username = %s""", (username,))
    data = cur.fetchall()
    try:
        conn.commit()
        return JSONResponse(content=data,
                            status_code=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    finally:
        # Close the database connection
        if cur:
            cur.close()
        if conn:
            conn.close()
    
@app.post("/notas/")
async def saveSong(cancion: Song):
    conn = connection.connection()
    cur = conn.cursor()

    try:
        cur.execute("""INSERT INTO songs (username, notas) 
                    VALUES(%s, %s)""", (cancion.username, cancion.song))
        conn.commit()
        return JSONResponse(content={"message": "Song saved successfully"},
                            status_code=status.HTTP_201_CREATED)

    except Exception as e:
        print(e)
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    finally:
        # Close the database connection
        if cur:
            cur.close()
        if conn:
            conn.close()
    
@app.delete("/notas/{id}")
async def deleteTempo(id: int):
    conn = connection.connection()
    cur = conn.cursor()
   
    try:
        cur.execute("""DELETE FROM songs WHERE id = %s""", (id,))
        conn.commit()
        return JSONResponse(content = {"message": "Song delete successfully"},
                            status_code = status.HTTP_200_OK)

    except Exception as e:
        print(e)
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    finally:
        # Close the database connection
        if cur:
            cur.close()
        if conn:
            conn.close()
#====================NOTAS=====================

#==================EMPAREJAR===================
@app.post("/emparejar")
async def createEmparejar(emparejar: Emparejar):
    conn = connection.connection()
    cur = conn.cursor()
    try:
        cur.execute("""INSERT INTO emparejar (actividad, imagen, audio, tipo) 
                    VALUES(%s, %s, %s, %s)""", (emparejar.actividad, emparejar.imagen,
                                                emparejar.audio, emparejar.tipo))
        conn.commit()
        return JSONResponse(content={"message": "Emparejar created successfully"},
                            status_code=status.HTTP_201_CREATED)
    except Exception as e:
        print(e)
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

@app.get("/emparejar")
async def showEmparejar():
    conn = connection.connection()
    cur = conn.cursor()

    try:
        cur.execute("""SELECT * FROM emparejar""")
        tempo = cur.fetchall()
        return JSONResponse(content= tempo, status_code=status.HTTP_200_OK)

    except Exception as e:
        print(e)
        return JSONResponse(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR)

@app.put("/emparejar/{id}")
async def updateEmparejar(id: int, new_data: Emparejar):
    conn = connection.connection()
    cur = conn.cursor()

    try:
        cur.execute("""UPDATE emparejar SET (actividad, imagen, audio, tipo)
                    WHERE id = %d, VALUES (%s, %s, %s, %s)""", (new_data.actividad,
                                                            new_data.imagen,
                                                            new_data.audio,
                                                            new_data.tipo))
        conn.commit()
        return JSONResponse(content= {"message": "Emparejar updated successfully"},
                            status_code=status.HTTP_200_OK)

    except Exception as e:
        print(e)
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

@app.delete("/Emparejar/{id}")
async def deleteEmparejar(id: int):
    conn = connection.connection()
    cur = conn.cursor()
   
    try:
        cur.execute("""DELETE FROM emparejar WHERE id = %d""", (id,))
        conn.commit()
        return JSONResponse(content = {"message": "Emparejar delete successfully"},
                            status_code = status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return JSONResponse(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR)
