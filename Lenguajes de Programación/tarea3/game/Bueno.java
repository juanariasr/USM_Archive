package game;

public class Bueno extends NPC{
        private String atributo;
        private int cantidad;

        /*Nombre: Bueno
        Como parametros recibe un String nombre que es el nombre del npc, un String atributo que es el atributo que el npc restaurara y un entero que es la cantidad que reestablecera dicho atributo
        Constructor*/
        public Bueno(String nombre, String atributo, int cantidad){
            super(nombre);
            this.atributo = atributo;
            this.cantidad = cantidad;
        }

        /*Nombre: set_atributo
        Como parametros recibe un String que es el atributo que se le asignara a la variable privada del mismo nombre
        */
        public void set_atributo(String atributo){ //SETTERS
            this.atributo = atributo;
        }
        /*Nombre: set_cantidad
        Como parametros recibe un entero que es al cantidad que se le asignara a la variable privada del mismo nombre
        */
        public void set_cantidad(int cantidad){
            this.cantidad = cantidad;
        }

        /*Nombre: get_atributo
        No recibe parametros
        retorna el valor de la variable atributo
        */
        public String get_atributo(){
            return atributo;
        }
        /*Nombre: get_cantidad
        No recibe parametros
        retorna el valor de la variable cantidad
        */
        public int get_cantidad(){
            return cantidad;
        }


        /*Nombre: interaccion
        Recibe un tipo jugador que corresponde al jugador
        Dependiendo del valor de la variable atributo aumenta una cierta cantidad dicho atributo
        Dicha cantidad esta dada por el valor de la variable cantidad
        */
        public void interaccion(Jugador player) {
            System.out.println(get_nombre() + ": " + player.get_nombre() + " senpai, creo que necesitas un poco de ayuda, por eso te subire " + get_cantidad() + " a tu " + get_atributo());
            if (atributo.equals("vida")){
                if (player.get_vida() + cantidad <= player.get_max_vida()){
                    player.set_vida(player.get_vida()+cantidad);
                } else {
                    System.out.println(get_nombre() + ": Te reestableci tu vida al maximo");
                    player.set_vida(player.get_max_vida());
                }
            } else if (atributo.equals("energia")){
                if (player.get_energia() + cantidad <= player.get_max_energia()){
                    player.set_energia(player.get_energia()+cantidad);
                } else {
                    System.out.println(get_nombre() + ": Te reestableci tu energia al maximo");
                    player.set_energia(player.get_max_energia());
                }
            } else if (atributo.equals("mana")){
                if (player.get_mana() + cantidad <= player.get_max_mana()){
                    player.set_mana(player.get_mana()+cantidad);
                } else {
                    System.out.println(get_nombre() + ": Te reestableci tu mana al maximo");
                    player.set_mana(player.get_max_mana());
                }
            } else {
                player.subir_experiencia(player.get_xp() + cantidad);
            }
            
            System.out.println(get_nombre() + ": Espero que con esta nueva cantidad de " + atributo + " derrotes a quien sea que quieras derrotar"); 
        }
    }

