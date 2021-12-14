package game;

import java.util.Random;

public class Planicie extends Tierra{
    /*Nombre: Planicie
    Como parametros recibe un flotante que corresponde a la probabilidad de que el monstruo aparezca, 
    un tipo Monstruo que corresponde al monstruo que puede haber en esta tierra, Un tipo Jefe_Final que corresponde al jefe final que puede haber en esta tierra,
    Un tipo NPC que corresponde al npc que puede estar en esta tierra
    Constructor*/
    public Planicie(float probabilidad_enemigo, Monstruos monstruo, Jefe_Final jefe_final, NPC npc){
        super(probabilidad_enemigo, monstruo, jefe_final, npc);
    }
    /*Nombre: accion
    Recibe un parametro player que corresponde al jugador
    Llama a las interacciones con el NPC (si existe) y con el enemigo que se encuentre presente
    Por ultimo revisa si al jugador le queda vida o no
    Si le queda vida retorna true
    Si no le queda vida retorna false*/
    public boolean accion(Jugador player) {
        System.out.println(player.get_nombre() + " entra a la planicie");
        if (get_npc() != null){
            System.out.println("Ya en la planicie " + player.get_nombre() + " se encuentra con alguien");
            get_npc().interaccion(player);
        } else{
            System.out.println(player.get_nombre() + ": Parece que no hay nadie en esta planicie");
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
        if (player.get_vida() > 0){
            System.out.println(player.get_nombre() + " a logrado salir de la planicie con " + player.get_vida() + " vida");
            return true;
        }
        System.out.println(player.get_nombre() + " perdio toda su vida en la planicie");
        return false;   
    }
}
