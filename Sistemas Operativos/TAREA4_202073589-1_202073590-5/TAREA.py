import threading
import random
import datetime
import time

#Total de personas
personas = 150
zona_comun_cant = personas
zona_comun_lock = threading.Lock()

#Semaforos and Locks
#Juego 1 : Montaña Rusa
juego1 = threading.Semaphore(0)
j1 = threading.Semaphore(10)
j1_cola = threading.Semaphore(10)
j1_lock = threading.Lock()

#Juego 2 : Casa de Terror 
juego2 = threading.Semaphore(0)
j2 = threading.Semaphore(2)
j2_cola = threading.Semaphore(8)
j2_lock = threading.Lock()

#Juego 3 : Carrusel 
juego3 = threading.Semaphore(0)
j3 = threading.Semaphore(5)
j3_cola = threading.Semaphore(15)
j3_lock = threading.Lock()

#Juego 4 : Barco Pirata
juego4 = threading.Semaphore(0)
j4 = threading.Semaphore(3)
j4_cola = threading.Semaphore(6)
j4_lock = threading.Lock()


#Capacidades y contadores de las partidas
capacidad1 = 10
capacidad2 = 2
capacidad3 = 5
capacidad4 = 3
count1 = 0
count2 = 0
count3 = 0
count4 = 0

#Escoger entre partidas
partidas = ["Montana_Rusa","Casa_de_Terror","Carrusel","Barco_Pirata"]

'''Archivos txt'''
zona = open("Zona_Comun.txt","w")
montana= open("Montana_Rusa.txt","w")
terror = open("Casa_Terror.txt","w")
carrusel = open("Carrusel.txt","w")
barco = open("Barco_Pirata.txt","w")
salida = open("Salida.txt","w")

def escribir(ingreso,choise,ctrl):

	if ctrl == 1:
		zona.write(threading.current_thread().name + ", " + 
        str(ingreso) + ", " + choise + ", " + 
        str(datetime.datetime.now().time()) + "\n")
	elif ctrl == 2:
		montana.write(threading.current_thread().name + ", " + 
        str(ingreso) + ", " + str(datetime.datetime.now().time()) + "\n")
	elif ctrl == 3:
		terror.write(threading.current_thread().name + ", " + 
        str(ingreso) + ", " + str(datetime.datetime.now().time()) + "\n")
	elif ctrl == 4:
		carrusel.write(threading.current_thread().name + ", " + 
        str(ingreso) + ", " + str(datetime.datetime.now().time()) + "\n")
	elif ctrl == 5:
		barco.write(threading.current_thread().name + ", " + 
        str(ingreso) + ", " + str(datetime.datetime.now().time()) + "\n")
	elif ctrl == 6:
		salida.write(threading.current_thread().name + ", " + 
        str(datetime.datetime.now().time()) + "\n")

def zona_comun():
    global count1
    global capacidad1
    global count2
    global capacidad2
    global count3
    global capacidad3
    global count4
    global capacidad4 
    
    ingreso = datetime.datetime.now().time()
    choise = random.choice(partidas)
    global zona_comun_cant
        
    if choise == "Montana_Rusa":
        j1_cola.acquire()
        zona_comun_lock.acquire()
        zona_comun_cant -= 1
        zona_comun_lock.release()
    
        ingreso1 = datetime.datetime.now().time()
        escribir(ingreso,choise,1)
        
        if (j1.acquire()):
            j1_cola.release()
            escribir(ingreso1,0,2)
            j1_lock.acquire()
            count1 += 1
            j1_lock.release()
            
            if count1 == capacidad1:
                time.sleep(9)
                for _ in range(capacidad1):
                    juego1.release()
                j1_lock.acquire()
                count1 = 0
                j1_lock.release()

            juego1.acquire()
            j1.release()
            escribir(0,0,6)
            
    elif choise == "Casa_de_Terror":
        j2_cola.acquire()
        zona_comun_lock.acquire()
        zona_comun_cant -= 1
        zona_comun_lock.release()
    
        ingreso2 = datetime.datetime.now().time()
        escribir(ingreso,choise,1)

        if (j2.acquire()):
            j2_cola.release()
            escribir(ingreso2,0,3)
            j2_lock.acquire()
            count2 += 1
            j2_lock.release()
            
            if count2 == capacidad2:
                time.sleep(5)
                for _ in range(capacidad2):
                    juego2.release()
                j2_lock.acquire()
                count2 = 0
                j2_lock.release()

            juego2.acquire()
            j2.release()
            escribir(0,0,6)
 
    elif choise == "Carrusel":
        j3_cola.acquire()
        zona_comun_lock.acquire()
        zona_comun_cant -= 1
        zona_comun_lock.release()
    
        ingreso3 = datetime.datetime.now().time()
        escribir(ingreso,choise,1)

        if (j3.acquire()):
            j3_cola.release()
            escribir(ingreso3,0,4)
            j3_lock.acquire()
            count3 += 1
            j3_lock.release()
            
            if count3 == capacidad3:
                time.sleep(7)
                for _ in range(capacidad3):
                    juego3.release()
                j3_lock.acquire()
                count3 = 0
                j3_lock.release()
                
            juego3.acquire()
            j3.release()
            escribir(0,0,6)
        
    elif choise == "Barco_Pirata":
        j4_cola.acquire()
        zona_comun_lock.acquire()
        zona_comun_cant -= 1
        zona_comun_lock.release()
    
        ingreso4 = datetime.datetime.now().time()
        escribir(ingreso,choise,1)

        if (j4.acquire()):
            j4_cola.release()
            escribir(ingreso4,0,5)
            j4_lock.acquire()
            count4 += 1
            j4_lock.release()
            
            if count4 == capacidad4:
                time.sleep(4)
                for _ in range(capacidad4):
                    juego4.release()

                j4_lock.acquire()
                count4 = 0
                j4_lock.release()

            juego4.acquire()
            j4.release()
            escribir(0,0,6)

####################################### Main #######################################

for n in range(personas):
    persona = threading.Thread(name='Persona%s'%(n+1), target = zona_comun)
    persona.start()
        
while zona_comun_cant != 0:
    time.sleep(1)
    
if zona_comun_cant == 0:
    time.sleep(1)
    if count1 != 0:
        time.sleep(9)
        for _ in range(count1):
            juego1.release()
        
    if count2 != 0:
        time.sleep(5)
        for _ in range(count2):
            juego2.release()
    
    if count3 != 0:
        time.sleep(7)
        for _ in range(count3):
            juego3.release()
            
    if count4 != 0:
        time.sleep(4)
        for _ in range(count4):
            juego4.release()
    
time.sleep(2)    

while threading.active_count() > 1:
    pass
else:
    zona.close()
    montana.close()
    terror.close()
    carrusel.close()
    barco.close()
    salida.close()

print("-"*20+"TERMINADO"+"-"*20)