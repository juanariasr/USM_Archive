from threading import Thread, Semaphore,Lock
import random,time
import datetime

SemaforoEstandarActivo = Semaphore(15)
SemaforoEstandarCola = Semaphore(7)

SemaforoVersusActivo = Semaphore(2)
SemaforoVersusCola = Semaphore(4)

SemaforoRapidaActivo = Semaphore(10)
SemaforoRapidaCola = Semaphore(8)

SemaforoEspecialActivo = Semaphore(12)
SemaforoEspecialCola = Semaphore(10)

lockLobby = Lock()
lockSalida = Lock()
lockJuegoEstandar = Lock()
lockJuegoVersus = Lock()
lockJuegoRapida = Lock()
lockJuegoEspecial = Lock()

EstandarEnJuego = 0
EstandarEnCola = 0

VersusEnJuego = 0
VersusEnCola  = 0

RapidaEnJuego = 0
RapidaEnCola = 0

EspecialEnJuego = 0
EspecialEnCola = 0

TotalJugadores = 120

class Jugador(Thread):
    def __init__(self, numero_hilo):
        Thread.__init__(self)
        self.numero_hilo = numero_hilo+1
        self.Juego = random.randint(0,3)

    def run(self): #Lobby
        time_entrarjuego = str(datetime.datetime.now())
        global TotalJugadores
        global EstandarEnJuego,VersusEnJuego,RapidaEnJuego,EspecialEnJuego
        global EstandarEnCola,VersusEnCola,RapidaEnCola,EspecialEnCola

        if (self.Juego==0):
            SemaforoEstandarCola.acquire() #Entra a la cola
            
            time_entrarcola = str(datetime.datetime.now())
            
            lockLobby.acquire()
            file = open("Lobby.txt","a")
            file.write("Jugador"+str(self.numero_hilo)+" "+time_entrarjuego+", Partida Estándar, "+time_entrarcola+"\n")
            file.close()
            TotalJugadores -= 1
            lockLobby.release()
            
            lockJuegoEstandar.acquire()
            EstandarEnCola += 1
            lockJuegoEstandar.release()
            
            SemaforoEstandarActivo.acquire()#Entra a la partida
            
            lockJuegoEstandar.acquire()
            EstandarEnCola -= 1
            lockJuegoEstandar.release()
            
            SemaforoEstandarCola.release()#Sale de la cola
            
            time_entrarpartida = str(datetime.datetime.now())
            
            lockJuegoEstandar.acquire()
            file = open("PartidaEstandar.txt","a")
            file.write("Jugador"+str(self.numero_hilo)+", "+time_entrarcola+", "+time_entrarpartida+"\n")
            file.close()
            EstandarEnJuego += 1
            lockJuegoEstandar.release()
            
            while EstandarEnJuego < 15 and TotalJugadores > (EstandarEnCola+VersusEnCola+RapidaEnCola+EspecialEnCola):
                print("Esperando jugador Partida Estándar...")
                
            time.sleep(7)
            
            lockJuegoEstandar.acquire()
            EstandarEnJuego -= 1
            lockJuegoEstandar.release()
            
            SemaforoEstandarActivo.release()#Sale de la partida
            
            
        elif(self.Juego==1):
            SemaforoVersusCola.acquire() #Entra a la cola
            
            lockLobby.acquire()
            time_entrarcola = str(datetime.datetime.now())
            file = open("Lobby.txt","a")
            file.write("Jugador"+str(self.numero_hilo)+" "+time_entrarjuego+", Partida Versus, "+time_entrarcola+"\n")
            file.close()
            TotalJugadores -= 1
            lockLobby.release()
            
            lockJuegoVersus.acquire()
            VersusEnCola += 1
            lockJuegoVersus.release()
            
            SemaforoVersusActivo.acquire()#Entra a la partida
            
            lockJuegoVersus.acquire()
            VersusEnCola -= 1
            lockJuegoVersus.release()
            
            SemaforoVersusCola.release()#Sale de la cola
            
            time_entrarpartida = str(datetime.datetime.now())
            
            lockJuegoVersus.acquire()
            file = open("PartidaVersus.txt","a")
            file.write("Jugador"+str(self.numero_hilo)+", "+time_entrarcola+", "+time_entrarpartida+"\n")
            file.close()
            VersusEnJuego += 1
            lockJuegoVersus.release()
            
            while VersusEnJuego < 2 and TotalJugadores > (EstandarEnCola+VersusEnCola+RapidaEnCola+EspecialEnCola):
                print("Esperando jugador Partida Versus...")
                
            time.sleep(3)
            
            lockJuegoVersus.acquire()
            VersusEnJuego -= 1
            lockJuegoVersus.release()
            
            SemaforoVersusActivo.release()#Sale de la partida

            
        elif (self.Juego==2):
            SemaforoRapidaCola.acquire() #Entra a la cola
            
            lockLobby.acquire()
            time_entrarcola = str(datetime.datetime.now())
            file = open("Lobby.txt","a")
            file.write("Jugador"+str(self.numero_hilo)+" "+time_entrarjuego+", Partida Rápida, "+time_entrarcola+"\n")
            file.close()
            TotalJugadores -= 1
            lockLobby.release()
            
            lockJuegoRapida.acquire()
            RapidaEnCola += 1
            lockJuegoRapida.release()
            
            SemaforoRapidaActivo.acquire()#Entra a la partida
            
            lockJuegoRapida.acquire()
            RapidaEnCola -= 1
            lockJuegoRapida.release()
            
            SemaforoRapidaCola.release()#Sale de la cola
            
            time_entrarpartida = str(datetime.datetime.now())
            
            lockJuegoRapida.acquire()
            file = open("PartidaRápida.txt","a")
            file.write("Jugador"+str(self.numero_hilo)+", "+time_entrarcola+", "+time_entrarpartida+"\n")
            file.close()
            RapidaEnJuego += 1
            lockJuegoRapida.release()
            
            while RapidaEnJuego < 10 and TotalJugadores > (EstandarEnCola+VersusEnCola+RapidaEnCola+EspecialEnCola):
                print("Esperando jugador Partida Rápida...")
                
            time.sleep(6)
            
            lockJuegoRapida.acquire()
            RapidaEnJuego -= 1
            lockJuegoRapida.release()
            
            SemaforoRapidaActivo.release()#Sale de la partida
            
            
        else:
            SemaforoEspecialCola.acquire() #Entra a la cola
            
            lockLobby.acquire()
            time_entrarcola = str(datetime.datetime.now())
            file = open("Lobby.txt","a")
            file.write("Jugador"+str(self.numero_hilo)+" "+time_entrarjuego+", Partida Especial Navidad, "+time_entrarcola+"\n")
            file.close()
            TotalJugadores -= 1
            lockLobby.release()
            
            lockJuegoEspecial.acquire()
            EspecialEnCola += 1
            lockJuegoEspecial.release()
            
            SemaforoEspecialActivo.acquire()#Entra a la partida
            
            lockJuegoRapida.acquire()
            RapidaEnCola -= 1
            lockJuegoRapida.release()
            
            SemaforoEspecialCola.release()#Sale de la cola
            
            time_entrarpartida = str(datetime.datetime.now())
            
            lockJuegoEspecial.acquire()
            file = open("PartidaEspecialNavidad.txt","a")
            file.write("Jugador"+str(self.numero_hilo)+", "+time_entrarcola+", "+time_entrarpartida+"\n")
            file.close()
            EspecialEnJuego += 1
            lockJuegoEspecial.release()
            
            while EspecialEnJuego < 12 and TotalJugadores > (EstandarEnCola+VersusEnCola+RapidaEnCola+EspecialEnCola):
                print("Esperando jugador Especial Navidad...")
                
            time.sleep(5)
            
            lockJuegoEspecial.acquire()
            RapidaEnJuego -= 1
            lockJuegoEspecial.release()
            
            SemaforoEspecialActivo.release()#Sale de la partida
            

        time_salir = str(datetime.datetime.now())
        
        lockLobby.acquire()
        file = open("Salida.txt","a")
        file.write("Jugador"+str(self.numero_hilo)+", "+time_salir+"\n")
        file.close()
        lockLobby.release()

'''
*****CrearArchivos*****
*No recibe valores de entrada

*Crea los archivos de texto para los registros.

1-. Abre/Crea un archivo llamado "Lobby.txt" en formato de escritura.
2-. Cierra el archivo recién abierto/creado.
3-. Repite pasos 1 y 2 para "PartidaEstandar.txt"
4-. Repite pasos 1 y 2 para "PartidaVersus.txt"
5-. Repite pasos 1 y 2 para "PartidaRápida.txt"
6-. Repite pasos 1 y 2 para "PartidaEspecialNavidad.txt"
7-. Repite pasos 1 y 2 para "Salida.txt"

*No retorna nada.
'''
def CrearArchivos():
    file = open("Lobby.txt","w")
    file.close()
    file = open("PartidaEstandar.txt","w")
    file.close()
    file = open("PartidaVersus.txt","w")
    file.close()
    file = open("PartidaRápida.txt","w")
    file.close()
    file = open("PartidaEspecialNavidad.txt","w")
    file.close()
    file = open("Salida.txt","w")
    file.close()

CrearArchivos()
for i in range(0,TotalJugadores):
   hilo=Jugador(i)
   hilo.start()
   #print ("Arrancado hilo "+str(i))



##COMENTAR!!


