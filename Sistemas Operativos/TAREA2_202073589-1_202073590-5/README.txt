Alonso Maureira - 202073589-1 - 200
Juan Arias - 202073590-5 - 200

Para la ejecución:
1.) Abrir la terminal en la carpeta de los archivos.
2.) Escribir "make".
Si se quiere ver de nuevo, "make clean" y después otro "make".

Especificaciones:

-A los bot se les asigna una fila aleatoria y pueden jugar solo en torno a esa fila.
-No pudimos implementar la tarea con fork() por lo cual creamos los jugadores a mano.
-jugador[0] es el jugador por consola.
-Se asume que el jugador por consola siempre jugara de manera correcta segun las reglas especificadas.
-El jugador por consola elige la fila y la carta que quiere jugar.
-Cuando se le pide el indice de la carta a jugar al jugador por consola se debe basar en lo siguiente:
    Indices 0   1   2   3   4   5   6 
    Cartas  12  13  13  15  17  40  29
-En las filas debe colocar el numero tal cual, las filas son 0,1,2,3.
