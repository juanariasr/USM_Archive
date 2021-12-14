package game;

import java.util.Scanner;

public class garage {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("Ahora el DM debe permitir al jugador crear su personaje");
        System.out.println("Mr jugador, eliga la opcion de la tierra que desea poner en esta casilla");
        System.out.println("1: Mago");
        System.out.println("2: Guerrero");
        System.out.println("3: Druida");
        System.out.print("Ingrese el numero de la opcion deseada: ");
        
        Jugador player = null;
        
        
        switch (Integer.parseInt(in.nextLine())) {
            case 1:
                System.out.print("Ingrese el nombre que le quiere dar a su personaje: ");
                player = new Mago(Main.entrada.nextLine());
                break;
            case 2:
                System.out.print("Ingrese el nombre que le quiere dar a su personaje: ");
                player = new Guerrero(Main.entrada.nextLine());
                break;
            case 3:
                System.out.print("Ingrese el nombre que le quiere dar a su personaje: ");
                player = new Druida(Main.entrada.nextLine());
            default:
                break;
        }

        NPC npc = new Bueno("Gamo-chan", "xp", 199);

        npc.interaccion(player);
        

        
        in.close();
    }
   
}
