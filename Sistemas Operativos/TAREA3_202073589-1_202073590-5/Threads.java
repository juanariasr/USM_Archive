import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

public class Threads {
    private static boolean encontrado = false; // Variable para controlar si se ha encontrado el tesoro

    public static void main(String[] args) throws IOException {
        //long startTime = System.nanoTime();
        // Leer el archivo de entrada ubicacion-tesoro.txt
        String filePath = "ubicacion-tesoro.txt";
        List<String> lineas = Files.readAllLines(Paths.get(filePath));

        // Obtener la dimensión de la matriz y el largo del tesoro
        int n = Integer.parseInt(lineas.get(0));
        int largoTesoro = Integer.parseInt(lineas.get(1));

        // Crear la matriz del mapa
        char[][] mapa = parsearMatriz(lineas.get(2), n);

        // Imprimir el mapa
        /*
        System.out.println("Mapa:");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(mapa[i][j] + " ");
            }
            System.out.println();
        }
        */
        // Buscar el tesoro utilizando múltiples hilos
        Thread hilo = new Thread(new BuscarTesoroThread(mapa, 0, n, 0, n, largoTesoro));
        hilo.start();

        //long endTime = System.nanoTime();

        //long elapsedTime = (endTime - startTime)/1000000;
        //System.out.println("Tiempo de ejecucion con threads: " + elapsedTime + " milisegundos");

    }

    private static char[][] parsearMatriz(String linea, int n) {
        char[][] matriz = new char[n][n];
        linea = linea.substring(1, linea.length() - 1); // Eliminar los corchetes
        String[] filas = linea.split("],\\[");
        for (int i = 0; i < n; i++) {
            String[] fila = filas[i].split(",");
            for (int j = 0; j < n; j++) {
                matriz[i][j] = fila[j].charAt(0);
            }
        }
        return matriz;
    }

    static synchronized void imprimirResultado(int fila, int columna) {
        if (!encontrado) {
            encontrado = true;
            System.out.println("Fila " + fila + ", columna " + columna);
        }
    }
}

class BuscarTesoroThread implements Runnable {
    private char[][] mapa;
    private int filaInicio;
    private int filaFin;
    private int columnaInicio;
    private int columnaFin;
    private int largoTesoro;

    public BuscarTesoroThread(char[][] mapa, int filaInicio, int filaFin, int columnaInicio, int columnaFin, int largoTesoro) {
        this.mapa = mapa;
        this.filaInicio = filaInicio;
        this.filaFin = filaFin;
        this.columnaInicio = columnaInicio;
        this.columnaFin = columnaFin;
        this.largoTesoro = largoTesoro;
    }

    @Override
    public void run() {
        if (filaFin - filaInicio <= largoTesoro && columnaFin - columnaInicio <= largoTesoro) {
            // Buscar el tesoro en el cuadrante actual
            for (int i = filaInicio; i < filaFin; i++) {
                for (int j = columnaInicio; j < columnaFin; j++) {
                    if (mapa[i][j] == 'x') {
                        Threads.imprimirResultado(i, j);
                    }
                }
            }
        } else {
            // Dividir el mapa en cuatro cuadrantes y crear un hilo para cada uno
            int filaMedia = (filaInicio + filaFin) / 2;
            int columnaMedia = (columnaInicio + columnaFin) / 2;

            Thread hilo1 = new Thread(new BuscarTesoroThread(mapa, filaInicio, filaMedia, columnaInicio, columnaMedia, largoTesoro));
            Thread hilo2 = new Thread(new BuscarTesoroThread(mapa, filaInicio, filaMedia, columnaMedia, columnaFin, largoTesoro));
            Thread hilo3 = new Thread(new BuscarTesoroThread(mapa, filaMedia, filaFin, columnaInicio, columnaMedia, largoTesoro));
            Thread hilo4 = new Thread(new BuscarTesoroThread(mapa, filaMedia, filaFin, columnaMedia, columnaFin, largoTesoro));

            // Iniciar los hilos
            hilo1.start();
            hilo2.start();
            hilo3.start();
            hilo4.start();

            // Esperar a que los hilos terminen
            try {
                hilo1.join();
                hilo2.join();
                hilo3.join();
                hilo4.join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
