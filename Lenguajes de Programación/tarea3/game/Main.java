package game;

import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static Scanner entrada = new Scanner(System.in);
    public static void main(String args[]){
        int world_size;
        System.out.println("Bienvenido a The Legend of Morio");
        System.out.print("Mister Dungeon Master ingrese el tamaño del mundo: ");
        
        world_size = Integer.parseInt(entrada.nextLine());
        List<Tierra> Mundo = new ArrayList<Tierra>(); 
        System.out.println("Mister DM prosiga a rellenar el mundo");

        List<Integer> jefes = new ArrayList<Integer>();

        for (int i = 0; i < world_size; i++){
            System.out.println("Eliga la opcion de la tierra que desea poner en esta casilla");
            System.out.println("1: Montaña");
            System.out.println("2: Planicie");
            System.out.println("3: Bosque");
            System.out.print("Ingrese el numero de la opcion deseada: ");
            Tierra tierra = null;
            
            int tipo_tierra = Integer.parseInt(entrada.nextLine());
            switch (tipo_tierra){
                case 1:
                    tierra = new Montana(0, null, null, null);
                    break;
                case 2:
                    tierra = new Planicie(0, null, null, null);
                    break;
                case 3:
                    tierra = new Bosque(0, null, null, null);
                    break;
                default:
                    break;
            }
            System.out.print("Ingrese la probabilidad de que un Enemigo aparezca (0.0-1.0): ");
            float probabilidad = Float.parseFloat(entrada.nextLine());
            tierra.set_probabilidad_enemigo(probabilidad);

            System.out.println("Eliga la opcion del tipo de Enemigo que podria aparecer");
            System.out.println("1: Monstruo");
            System.out.println("2: Jefe Final");
            System.out.print("Ingrese el numero de la opcion deseada: ");
            
            int vida, dano, tipo_enemigo;
            tipo_enemigo = Integer.parseInt(entrada.nextLine());
            switch (tipo_enemigo) {
                case 1:
                    System.out.print("Ingrese la cantidad de vida del monstruo: ");
                    vida = Integer.parseInt(entrada.nextLine());
                    System.out.print("Ingrese la cantidad de daño que el monstruo inflingira en el jugador: ");
                    dano = Integer.parseInt(entrada.nextLine());
                    tierra.set_monstruo(new Monstruos(vida, dano));
                    tierra.get_monstruo().set_existe(true);
                    tierra.set_jefe_final(new Jefe_Final(null, 0, 0));
                    break;
                case 2:
                    String nombre_jf; 
                    System.out.print("Ingrese el nombre del jefe final: ");
                    nombre_jf = entrada.nextLine();
                    System.out.print("Ingrese la cantidad de vida del jefe final: ");
                    vida = Integer.parseInt(entrada.nextLine());
                    System.out.print("Ingrese la cantidad de daño base que el jefe final inflingira en el jugador: ");
                    dano = Integer.parseInt(entrada.nextLine());
                    tierra.set_monstruo(new Monstruos(0, 0));
                    tierra.set_jefe_final(new Jefe_Final(nombre_jf, vida, dano));
                    jefes.add(i);
                    break;
                default:
                    break;
            }

            System.out.println("Mister DM, habra un NPC aca?");
            System.out.print("Ingrese un '1' si la respuesta es si, en el caso contrario ingrese un '0': ");
            NPC npc = null;
            String nom_npc;
            int hay_npc = Integer.parseInt(entrada.nextLine());
            if (hay_npc == 1){
                String atributo;
                int cantidad;
                System.out.println("Eliga la opcion del tipo de NPC que quiere insertar");
                System.out.println("1: Bueno");
                System.out.println("2: Neutro");
                System.out.println("3: Malo");
                System.out.print("Ingrese el numero de la opcion deseada: ");
                int tipo_npc = Integer.parseInt(entrada.nextLine());
                switch (tipo_npc){
                    case 1:
                        System.out.print("Ingrese el nombre del npc: ");
                        nom_npc = entrada.nextLine();
                        System.out.print("Ingrese el atributo del npc (vida/mana/energia/xp): ");
                        atributo = entrada.nextLine();
                        System.out.print("Ingrese la cantidad en la que el npc aumentara el atributo: ");
                        cantidad = Integer.parseInt(entrada.nextLine());
                        npc = new Bueno(nom_npc, atributo, cantidad);
                        break;
                    case 2:
                        char requisito;
                        int valor, recompensa;
                        System.out.print("Ingrese el nombre del npc: ");
                        nom_npc = entrada.nextLine();
                        System.out.print("Ingrese el requisito del npc (v/m): ");
                        requisito = entrada.nextLine().charAt(0);
                        System.out.print("Ingrese el valor que tiene que cumplir el jugador para completar la mision: ");
                        valor = Integer.parseInt(entrada.nextLine());
                        System.out.print("Ingrese la cantidad de xp que el npc le dara al jugador: ");
                        recompensa = Integer.parseInt(entrada.nextLine());
                        npc = new Neutro(nom_npc, requisito, valor, recompensa);
                        break;
                    case 3:
                        System.out.print("Ingrese el nombre del npc: ");
                        nom_npc = entrada.nextLine();
                        System.out.print("Ingrese la cantidad de energia que el npc le disminuira al jugador: ");
                        int cant_energia = Integer.parseInt(entrada.nextLine());
                        System.out.print("Ingrese la cantidad de mana que el npc le disminuira al jugador: ");
                        int cant_mana = Integer.parseInt(entrada.nextLine());
                        npc = new Malo(nom_npc, cant_energia, cant_mana);
                        break;
                }
                tierra.set_npc(npc);
            }  
            Mundo.add(i, tierra);
            System.out.println("Nos movemos a la siguiente casilla Mister DM");
            System.out.println(" ");

        }//aca termina el for

        System.out.print("DM, despues de hacer tan laboriosa tarea, ingresa la posicion inicial del jugador: ");
        int posicion_inicial = Integer.parseInt(entrada.nextLine());
        System.out.println("Ahora el DM debe permitir al jugador crear su personaje");
        System.out.println("Mister jugador, elija el tipo de pesonaje que desea ser");
        System.out.println("1: Mago");
        System.out.println("2: Guerrero");
        System.out.println("3: Druida");
        System.out.print("Ingrese el numero de la opcion deseada: ");

        Jugador player = null;
        
        int tipo_jugador = Integer.parseInt(entrada.nextLine());
        switch (tipo_jugador) {
            case 1:
                System.out.print("Ingrese el nombre que le quiere dar a su personaje: ");
                player = new Mago(entrada.nextLine());
                break;
            case 2:
                System.out.print("Ingrese el nombre que le quiere dar a su personaje: ");
                player = new Guerrero(entrada.nextLine());
                break;
            case 3:
                System.out.print("Ingrese el nombre que le quiere dar a su personaje: ");
                player = new Druida(entrada.nextLine());
                break;
            default:
                break;
        }
        player.set_posicion_actual(posicion_inicial);

        boolean condicion_de_termino = false;

        while (condicion_de_termino == false){
            System.out.println(" ");
            System.out.println("|___Menu de Juego___|");
            System.out.println("La vida de " + player.get_nombre() + " es " + player.get_vida());
            System.out.println("La cantidad de xp de " + player.get_nombre() + " es " + player.get_xp());
            System.out.println("La fuerza de " + player.get_nombre() + " es " + player.get_fuerza());
            System.out.println("La inteligencia de " + player.get_nombre() + " es " + player.get_inteligencia());
            System.out.println("La energia de " + player.get_nombre() + " es " + player.get_energia());
            System.out.println("El mana de " + player.get_nombre() + " es " + player.get_mana());
            System.out.println("La lista de misiones de " + player.get_nombre() + " es " + player.get_lista_misiones());
            System.out.print("Quieres avanzar hacia la derecha (1) o a la izquierda (2): ");
            int movimiento = Integer.parseInt(entrada.nextLine());
            System.out.println("|___________________|");
            System.out.println(" ");

            switch (movimiento) {
                case 1:
                    if (player.get_posicion_actual()+1 == Mundo.size()){
                        player.set_posicion_actual(0);
                        
                    } else{
                        player.set_posicion_actual(player.get_posicion_actual()+1);
                    }           
                    break;
                case 2:
                    if (player.get_posicion_actual()-1 < 0){
                        player.set_posicion_actual(Mundo.size()-1);
                    } else{
                        player.set_posicion_actual(player.get_posicion_actual()-1);
                    }
                    break;
                default:
                    break;
            }
            boolean status = Mundo.get(player.get_posicion_actual()).accion(player);
            if (status == false){
                if (player.get_vida() <= 0){
                    System.out.println(" ");
                    System.out.println("Game Over por muerte del personaje RIP in Pieces");
                    player.set_vida(0);
                    condicion_de_termino = true;
                } else{
                    if (movimiento == 1){
                        if (player.get_posicion_actual()-1 < 0){
                            player.set_posicion_actual(Mundo.size()-1);
                        } else{
                            player.set_posicion_actual(player.get_posicion_actual()-1);
                        }
                    } else {
                        if (player.get_posicion_actual()+1 == Mundo.size()){
                            player.set_posicion_actual(0);
                        } else{
                            player.set_posicion_actual(player.get_posicion_actual()+1);
                        }  
                    }
                }
            }
            for (int i = 0; i < player.get_lista_misiones().size(); i++){
                if (Character.compare(player.get_lista_misiones().get(i).get_requisito(), 'v') == 0){
                    player.get_lista_misiones().get(i).set_cantidad(player.get_posicion_actual());
                }
            }     
            if (jefes.contains(player.get_posicion_actual()) && condicion_de_termino == false && Mundo.get(player.get_posicion_actual()).get_jefe_final().get_status_combate()){
                System.out.println(" ");
                System.out.println("Ganaste porque mataste un jefe final");
                condicion_de_termino = true;
            }
            if (condicion_de_termino == false){
                for (int i = 0; i < player.get_lista_misiones().size(); i++){
                    if (Character.compare(player.get_lista_misiones().get(i).get_requisito(), 'v') == 0){ //necesito hacerlo asi para poder dar las recompensas de la mision
                        if (player.get_lista_misiones().get(i).get_valor() == player.get_lista_misiones().get(i).get_cantidad()){
                            player.subir_experiencia(player.get_lista_misiones().get(i).get_recompensa());
                            player.get_lista_misiones().remove(i);
                        }
                    } else if(Character.compare(player.get_lista_misiones().get(i).get_requisito(), 'm') == 0){
                        if (player.get_lista_misiones().get(i).get_valor() == player.get_lista_misiones().get(i).get_cantidad()){
                            player.subir_experiencia(player.get_lista_misiones().get(i).get_recompensa());
                            player.get_lista_misiones().remove(i);
                        }
                    }
                }
            }
        }
        System.out.println(" ");
        System.out.println("|___Estadisticas Finales___|");
        System.out.println("La vida de " + player.get_nombre() + " es " + player.get_vida());
        System.out.println("La cantidad de xp de " + player.get_nombre() + " es " + player.get_xp());
        System.out.println("La fuerza de " + player.get_nombre() + " es " + player.get_fuerza());
        System.out.println("La inteligencia de " + player.get_nombre() + " es " + player.get_inteligencia());
        System.out.println("La energia de " + player.get_nombre() + " es " + player.get_energia());
        System.out.println("El mana de " + player.get_nombre() + " es " + player.get_mana());
        entrada.close();   
    }
}