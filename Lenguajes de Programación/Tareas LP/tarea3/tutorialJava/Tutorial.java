package tutorialJava;

import java.util.Scanner; //Esta libreria sirve para inputs por consola

public class Tutorial { //la clase se llama tutorial igual que el archivo
        public static void main(String args[]){
        System.out.println("Hello World!");

        int num_uno = 5; 
        int num_dos = 1;
        int resultado;
        resultado = num_uno + num_dos;
        System.out.println("El valor de la suma es: " + resultado); //el + es concatenacion

        if (resultado > 6){
            System.out.println("En efecto el resultado es mayor a 6: " + resultado);
        }
        else if (resultado < 6){
            System.out.println("No compa no es mayor a 6: " + resultado);
        }
        else {
            System.out.println("El resultado es 6: " + resultado);
        }

        Scanner entrada = new Scanner(System.in);//la variable es tipo Scanner
        String nombre = "";
        int numUno, numDos, result;
        System.out.println("Cual es tu nombre petizo?");
        nombre = entrada.nextLine(); //El metodo cambia segun sea el tipo de dato de entrada
        System.out.println("Dame el primer valor para tu suma: ");
        numUno = entrada.nextInt();
        System.out.println("Dame el segundo valor para tu suma: ");
        numDos = entrada.nextInt();
        result = numUno + numDos;
        System.out.println("Tu nombre es " + nombre + " y tu suma es " + result);
        entrada.close();

        int llave = 1;
        switch (llave) {
            case 1:
                System.out.println("Entro en el caso 1");
                break;
            default:
            System.out.println("RIP in pieces switch");
                break;
        }

        for(int i = 0; i < 5; i++){
            System.out.print(i + ", "); //println se ocupa cuando se quiere un salto de linea, en el caso contrario se usa nada mas print
        }
        System.out.println("");

        int wail = 0;
        while (wail < 7){
            System.out.print(wail + ", ");
            wail += 2;
        }
        System.out.println("");

        int waildo = 1000;
        do{
            System.out.print(waildo+", ");
            waildo -= 200;
        }while(waildo >= 0);
        System.out.println("");

        //existe un metodo .equals que compara strings, no se si sea util pa la tarea por eso lo dejo en stand by y tambien hay un monton de manipulacion de strings

        int numeros[] = new int[5]; //estatico
        for (int i = 0; i < 5; i++){
            numeros[i] = i;
        }
        for (int i = 0; i < numeros.length; i++){
            System.out.print(numeros[i] + ", ");
        }
        System.out.println("");
    }
} 