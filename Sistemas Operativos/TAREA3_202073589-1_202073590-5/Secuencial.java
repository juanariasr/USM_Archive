import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

public class Secuencial {
    public static void main(String[] args) {
        //long startTime = System.nanoTime();
        String filePath = "ubicacion-tesoro.txt";
        List<String> lineas;
        try {
            lineas = Files.readAllLines(Paths.get(filePath));

            // Obtener la dimensión de la matriz y el largo del tesoro
            int n = Integer.parseInt(lineas.get(0));
            int largoTesoro = Integer.parseInt(lineas.get(1));

            // Crear la matriz del mapa
            char[][] mapa = parsearMatriz(lineas.get(2), n);

            // Búsqueda horizontal
            busquedaSecuencial(mapa, largoTesoro);

            //long endTime = System.nanoTime();

            //long elapsedTime = (endTime - startTime)/1000000;

            //System.out.println("Tiempo de ejecucion sin nada: " + elapsedTime + " milisegundos");
        } catch (IOException e) {
            System.out.println("Error al leer el archivo: " + e.getMessage());
        }
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

    private static void busquedaSecuencial(char[][] mapa, int largoTesoro) {
        int n = mapa.length;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= n - largoTesoro; j++) {
                boolean encontrado = true;
                for (int k = 0; k < largoTesoro; k++) {
                    if (mapa[i][j + k] != 'x') {
                        encontrado = false;
                        break;
                    }
                }
                if (encontrado) {
                    System.out.println("Fila " + i + ", columna " + j);
                    return; // Detener la búsqueda después de encontrar la primera secuencia
                }
            }
        }
        System.out.println("No se encontró ninguna secuencia horizontal de tamaño " + largoTesoro);
    }
}

