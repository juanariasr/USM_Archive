package game;

import java.util.Random;

public class Bosque extends Tierra{

    /*Nombre: Bosque
    Como parametros recibe un flotante que corresponde a la probabilidad de que el monstruo aparezca, 
    un tipo Monstruo que corresponde al monstruo que puede haber en esta tierra, Un tipo Jefe_Final que corresponde al jefe final que puede haber en esta tierra,
    Un tipo NPC que corresponde al npc que puede estar en esta tierra
    Constructor*/
    public Bosque(float probabilidad_enemigo, Monstruos monstruo, Jefe_Final jefe_final, NPC npc){
        super(probabilidad_enemigo, monstruo, jefe_final, npc);
    }

    /*Nombre: accion
    Recibe un parametro player que corresponde al jugador
    Primero revisa si el jugador tiene mana mayor a cero para poder entrar.
    Si tiene hace los calculos necesarios para actualizar el valor de la mana y de la vida si es necesaria
    Posteriormente llama a las interacciones con el NPC (si existe) y con el enemigo que se encuentre presente
    Por ultimo revisa si al jugador le queda vida o no
    Si le queda vida retorna true
    Si no le queda vida o no tuvo suficiente energia para entrar al bosque retorna false*/
    public boolean accion(Jugador player) {
        System.out.println(player.get_nombre() + " intenta entrar en el bosque");
        if (player.get_mana() > 0){
            System.out.println(player.get_nombre() + " logra entrar al bosque ya que tiene " + player.get_mana() + " mana disponible");
            player.set_mana(player.get_mana()-3);
            if (player.get_mana() < 0){
                System.out.println(player.get_nombre() + " no tuvo suficiente mana y por eso tuvo que ocupar un poco de su vida");
                System.out.println("Esto es lo que se va a restar de la vida: " + player.get_mana());
                player.set_vida(player.get_vida() + player.get_mana());
                player.set_mana(0);
            }
            System.out.println("A " + player.get_nombre() + " le queda " + player.get_mana() + " mana disponible");
            if (player.get_vida() >= 0){
                if (get_npc() != null){
                    System.out.println("Ya en el bosque " + player.get_nombre() + " se encuentra con alguien");
                    get_npc().interaccion(player);
                } else{
                    System.out.println(player.get_nombre() + ": Parece que no hay nadie en este bosque");
                }
                Random random = new Random();
                if (random.nextFloat(1.0f) <= get_probabilidad_enemigo()){
                    if (get_monstruo().get_existe()){
                        get_monstruo().combate(player);
                    } else if (get_jefe_final().get_nombre() != null){
                        System.out.println("De repente, un jefe final aparece");
                        get_jefe_final().combate(player);
                    }
                }
            }
            if (player.get_vida() > 0){
            System.out.println(player.get_nombre() + " a logrado salir del bosque con " + player.get_vida() + " vida");
            return true;
            }
            System.out.println(player.get_nombre() + " perdio toda su vida y perecio en el bosque");
            return false;
        } else {
            System.out.println(player.get_nombre() + " no a podido entrar al bosque porque no tiene mana");
            return false;
        }
    }
}
