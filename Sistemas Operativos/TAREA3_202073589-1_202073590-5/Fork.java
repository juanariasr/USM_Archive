import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.concurrent.ForkJoinPool;
import java.util.concurrent.RecursiveTask;

public class Fork {
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

        // Buscar el tesoro utilizando múltiples hilos
        ForkJoinPool pool = new ForkJoinPool();
        BuscarTesoroTask tareaPrincipal = new BuscarTesoroTask(mapa, 0, n, 0, n, largoTesoro);
        pool.invoke(tareaPrincipal);

        //long endTime = System.nanoTime();

        //long elapsedTime = (endTime - startTime)/1000000;
        //System.out.println("Tiempo de ejecucion con fork: " + elapsedTime + " milisegundos");
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

    //Imprime en el formato pedido
    static synchronized void imprimirResultado(int fila, int columna) {
        if (!encontrado) {
            encontrado = true;
            System.out.println("Fila " + fila + ", columna " + columna);
        }
    }
}

class BuscarTesoroTask extends RecursiveTask<Void> {
    private char[][] mapa;
    private int filaInicio;
    private int filaFin;
    private int columnaInicio;
    private int columnaFin;
    private int largoTesoro;

    public BuscarTesoroTask(char[][] mapa, int filaInicio, int filaFin, int columnaInicio, int columnaFin, int largoTesoro) {
        this.mapa = mapa;
        this.filaInicio = filaInicio;
        this.filaFin = filaFin;
        this.columnaInicio = columnaInicio;
        this.columnaFin = columnaFin;
        this.largoTesoro = largoTesoro;
    }

    @Override
    protected Void compute() {
        if (filaFin - filaInicio <= largoTesoro && columnaFin - columnaInicio <= largoTesoro) {
            // Buscar el tesoro en el cuadrante actual
            for (int i = filaInicio; i < filaFin; i++) {
                for (int j = columnaInicio; j < columnaFin; j++) {
                    if (mapa[i][j] == 'x') {
                        Fork.imprimirResultado(i, j);
                    }
                }
            }
        } else {
            // Dividir el mapa en cuatro cuadrantes y crear una tarea para cada uno
            int filaMedia = (filaInicio + filaFin) / 2;
            int columnaMedia = (columnaInicio + columnaFin) / 2;

            BuscarTesoroTask tarea1 = new BuscarTesoroTask(mapa, filaInicio, filaMedia, columnaInicio, columnaMedia, largoTesoro);
            BuscarTesoroTask tarea2 = new BuscarTesoroTask(mapa, filaInicio, filaMedia, columnaMedia, columnaFin, largoTesoro);
            BuscarTesoroTask tarea3 = new BuscarTesoroTask(mapa, filaMedia, filaFin, columnaInicio, columnaMedia, largoTesoro);
            BuscarTesoroTask tarea4 = new BuscarTesoroTask(mapa, filaMedia, filaFin, columnaMedia, columnaFin, largoTesoro);

            // Ejecutar las tareas de manera concurrente
            invokeAll(tarea1, tarea2, tarea3, tarea4);
        }
        return null;
    }
}
