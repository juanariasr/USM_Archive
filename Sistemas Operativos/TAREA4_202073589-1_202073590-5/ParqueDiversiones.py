import threading
import time
import random

"""
Nombre: registrar_actividad
Parametros: persona_id, atraccion, tiempo_inicio_fila, tiempo_ingreso_atraccion, num_atraccion
Descripcion: Registra la actividad de una persona en una atraccion, guardando los datos en la lista correspondiente.
"""
def registrar_actividad(persona_id, atraccion, tiempo_inicio_fila, tiempo_ingreso_atraccion, num_atraccion):
    registro = f"Persona{persona_id}, {tiempo_inicio_fila}, {tiempo_ingreso_atraccion}, {num_atraccion}"
    if atraccion == "Montaña Rusa":
        registros_montana_rusa.append(registro)
    elif atraccion == "Casa Terror":
        registros_casa_terror.append(registro)
    elif atraccion == "Carrusel":
        registros_carrusel.append(registro)
    elif atraccion == "Barco Pirata":
        registros_barco_pirata.append(registro)


"""
Nombre: escribir_archivo
Parametros: nombre_archivo, registros
Descripcion: Escribe los registros de una lista en un archivo de texto.
"""
def escribir_archivo(nombre_archivo, registros):
    contenido = "\n".join(registros)
    with open(nombre_archivo, "w") as archivo:
        archivo.write(contenido)

"""
Nombre: persona
Parametros: persona_id
Descripcion: Simula el comportamiento de una persona en el parque de diversiones, donde la persona ingresa al parque,
se dirige a una atraccion, espera en la fila, ingresa a la atraccion, espera en la fila de la segunda atraccion,
ingresa a la segunda atraccion y finalmente sale del parque.
"""
def persona(persona_id):
    global personas_dentro

    tiempo_ingreso = time.time()

    with contador_personas:
        personas_dentro += 1

    atracciones = ["Montaña Rusa", "Casa Terror", "Carrusel", "Barco Pirata"]
    random.shuffle(atracciones)

    primera_atraccion = atracciones[0]
    segunda_atraccion = atracciones[1]

    tiempo_inicio_fila = None
    tiempo_ingreso_atraccion = None

    tiempo_inicio_fila2 = None
    tiempo_ingreso_atraccion2 = None

    if primera_atraccion == "Montaña Rusa":
        tiempo_inicio_fila = time.time()
        with fila_montana_rusa:
            tiempo_ingreso_atraccion = time.time()
            time.sleep(duracion_montana_rusa) #Tiempo que demora la atraccion
            acceso_montana_rusa.acquire()
            acceso_montana_rusa.release()
            registrar_actividad(persona_id, "Montaña Rusa", tiempo_inicio_fila, tiempo_ingreso_atraccion, 1)

    elif primera_atraccion == "Casa Terror":
        tiempo_inicio_fila = time.time()
        with fila_casa_terror:
            tiempo_ingreso_atraccion = time.time() 
            time.sleep(duracion_casa_terror) #Tiempo que demora la atraccion
            acceso_casa_terror.acquire()
            acceso_casa_terror.release()
            registrar_actividad(persona_id, "Casa Terror", tiempo_inicio_fila, tiempo_ingreso_atraccion, 1)

    elif primera_atraccion == "Carrusel":
        tiempo_inicio_fila = time.time()
        with fila_carrusel:
            tiempo_ingreso_atraccion = time.time()
            time.sleep(duracion_carrusel) #Tiempo que demora la atraccion
            acceso_carrusel.acquire()
            acceso_carrusel.release()
            registrar_actividad(persona_id, "Carrusel", tiempo_inicio_fila, tiempo_ingreso_atraccion, 1)

    elif primera_atraccion == "Barco Pirata":
        tiempo_inicio_fila = time.time()
        with fila_barco_pirata:
            tiempo_ingreso_atraccion = time.time()
            time.sleep(duracion_barco_pirata) #Tiempo que demora la atraccion
            acceso_barco_pirata.acquire()
            acceso_barco_pirata.release()
            registrar_actividad(persona_id, "Barco Pirata", tiempo_inicio_fila, tiempo_ingreso_atraccion, 1)

    if segunda_atraccion == "Montaña Rusa":
        tiempo_inicio_fila2 = time.time()
        with fila_montana_rusa:
            tiempo_ingreso_atraccion2 = time.time()
            time.sleep(duracion_montana_rusa) #Tiempo que demora la atraccion
            acceso_montana_rusa.acquire()
            acceso_montana_rusa.release()
            registrar_actividad(persona_id, "Montaña Rusa", tiempo_inicio_fila2, tiempo_ingreso_atraccion2, 2)

    elif segunda_atraccion == "Casa Terror":
        tiempo_inicio_fila2 = time.time()
        with fila_casa_terror:
            tiempo_ingreso_atraccion2 = time.time()
            time.sleep(duracion_casa_terror) #Tiempo que demora la atraccion
            acceso_casa_terror.acquire()
            acceso_casa_terror.release()
            registrar_actividad(persona_id, "Casa Terror", tiempo_inicio_fila2, tiempo_ingreso_atraccion2, 2)

    elif segunda_atraccion == "Carrusel":
        tiempo_inicio_fila2 = time.time()
        with fila_carrusel:
            tiempo_ingreso_atraccion2 = time.time()
            time.sleep(duracion_carrusel) #Tiempo que demora la atraccion
            acceso_carrusel.acquire()
            acceso_carrusel.release()
            registrar_actividad(persona_id, "Carrusel", tiempo_inicio_fila2, tiempo_ingreso_atraccion2, 2)

    elif segunda_atraccion == "Barco Pirata":
        tiempo_inicio_fila2 = time.time()
        with fila_barco_pirata:
            tiempo_ingreso_atraccion2 = time.time()
            time.sleep(duracion_barco_pirata) #Tiempo que demora la atraccion
            acceso_barco_pirata.acquire()
            acceso_barco_pirata.release()
            registrar_actividad(persona_id, "Barco Pirata", tiempo_inicio_fila2, tiempo_ingreso_atraccion2, 2)

    tiempo_salida_parque = time.time()
    registro_salida = f"Persona{persona_id}, {tiempo_salida_parque}"
    with lock:
        registros_salida.append(registro_salida)

    with lock:
        registros_zona_comun.append(f"Persona{persona_id},{tiempo_ingreso} ,{primera_atraccion}, {tiempo_inicio_fila}, {segunda_atraccion}, {tiempo_inicio_fila2}")
        if personas_dentro == 1:
            escribir_archivo("ZonaComun.txt", registros_zona_comun)
            escribir_archivo("MontanaRusa.txt", registros_montana_rusa)
            escribir_archivo("CasaTerror.txt", registros_casa_terror)
            escribir_archivo("Carrusel.txt", registros_carrusel)
            escribir_archivo("BarcoPirata.txt", registros_barco_pirata)
            registros_zona_comun.clear()
            registros_montana_rusa.clear()
            registros_casa_terror.clear()
            registros_carrusel.clear()
            registros_barco_pirata.clear()

        personas_dentro -= 1

    #print(f"Persona{persona_id} ha completado las atracciones.")



capacidad_montana_rusa = 10
duracion_montana_rusa = 9

capacidad_casa_terror = 8
duracion_casa_terror = 5

capacidad_carrusel = 15
duracion_carrusel = 7

capacidad_barco_pirata = 6
duracion_barco_pirata = 4

fila_montana_rusa = threading.Semaphore(capacidad_montana_rusa)
fila_casa_terror = threading.Semaphore(capacidad_casa_terror)
fila_carrusel = threading.Semaphore(capacidad_carrusel)
fila_barco_pirata = threading.Semaphore(capacidad_barco_pirata)

acceso_montana_rusa = threading.Lock()
acceso_casa_terror = threading.Lock()
acceso_carrusel = threading.Lock()
acceso_barco_pirata = threading.Lock()

registros_zona_comun = []
registros_montana_rusa = []
registros_casa_terror = []
registros_carrusel = []
registros_barco_pirata = []
registros_salida = []

lock = threading.Lock()
contador_personas = threading.Lock()
personas_dentro = 0
num_personas = 150
threads = []
for i in range(num_personas):
    t = threading.Thread(target=persona, args=(i+1,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

escribir_archivo("Salida.txt", registros_salida)