package game;

import java.util.Random;

public class Malo extends NPC{
    private int cantidad_energia;
    private int cantidad_mana;

    /*Nombre: Malo
    Como parametros recibe un String nombre que es el nombre del npc, un entero cantidad_energia que corresponde a la cantidad de energia que el npc restara al jugador
    y un entero cantidad_mana la cantidad de mana queel npc restara al jugador
    Constructor*/
    public Malo(String nombre, int cantidad_energia, int cantidad_mana){
        super(nombre);
        this.cantidad_energia = cantidad_energia;
        this.cantidad_mana = cantidad_mana;
    }
    /*Nombre: set_cantidad_energia
    Como parametros recibe un entero que es al cantidad de energia que se le asignara a la variable privada cantidad_energia
    */
    public void set_cantidad_energia(int cantidad){ //SETTERS
        this.cantidad_energia = cantidad;
    }
    /*Nombre: set_cantidad_mana
    Como parametros recibe un entero que es al cantidad de mana que se le asignara a la variable privada cantidad_mana
    */
    public void set_cantidad_mana(int cantidad){
        this.cantidad_mana = cantidad;
    }

    /*Nombre: get_cantidad_energia
    Retorna el valor de la variable cantidad_energia
    */
    public int get_cantidad_energia(){ //GETTERS
        return cantidad_energia;
    }
    /*Nombre: get_cantidad_mana
    Retorna el valor de la variable cantidad_mana
    */
    public int get_cantidad_mana(){
        return cantidad_mana;
    }

    /*Nombre: interaccion
    Haciendo uso de una variable random maneja si el npc malo le bajara la energia y/o el mana al jugador
    */
    public void interaccion(Jugador player){
        Random random = new Random();
        System.out.println(get_nombre() + ": Soy un pibe re malardo y dependiendo de tu suerte te voy a bajar tu energia y/o tu mana");
        System.out.println(get_nombre() + ": Esperemos que tus " + player.get_energia() + " puntos de energia y " + player.get_mana() + " puntos de mana no se vean afectados juas juas juas");
        if (random.nextInt(6)+1 <= 11){
            if (player.get_energia() - cantidad_energia > 0){
                System.out.println(get_nombre() + ": Mala suerte crack, te voy a disminuir tu energia en " + cantidad_energia);
                player.set_energia(player.get_energia() - cantidad_energia);
            } else {
                System.out.println(get_nombre() + ": Lastima por ti compa, tu energia quedo en 0");
                player.set_energia(0);
            }
        }
        if (random.nextInt(6)+1 <= 11){
            if (player.get_mana() - cantidad_mana > 0){
                System.out.println(get_nombre() + ": Mala suerte crack, te voy a disminuir tu mana en " + cantidad_mana);
                player.set_mana(player.get_mana() - cantidad_mana);          
            } else {
                System.out.println(get_nombre() + ": Lastima por ti compa, tu mana quedo en 0");
                player.set_mana(0); //hay un problema con el set mana
            }
        }
    }
}
