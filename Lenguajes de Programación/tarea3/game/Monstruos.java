package game;



public class Monstruos implements Enemigos{
    private int vida;
    private int dano;
    private boolean status_vida_monstruo; //variable que determina si el monstruo a sido derrotado o no por si se visita la misma casilla
    private boolean existe;

    /*Nombre: Monstruos
    Como parametros recibe dos enteros que representan la vida y el dano del monstruo
    Constructor*/
    public Monstruos(int vida, int dano){
        this.vida = vida;
        this.dano = dano;
        status_vida_monstruo = true; //true = el monstruo esta vivo
        existe = false;
    }
    //SETTERS de la clase monstruos
    public void set_vida(int vida){ 
        this.vida = vida;
    }
    public void set_dano(int dano){
        this.dano= dano;
    }
    public void set_status_vida_monstruo(boolean status_vida_monstruo){
        this.status_vida_monstruo = status_vida_monstruo;
    }
    public void set_existe(boolean existe){
        this.existe = existe;
    }

    //GETTERS de la clase monstruos
    public int get_vida(){ 
        return vida;
    }
    public int get_dano(){
        return dano;
    }
    public boolean get_status_vida_monstruo(){
        return status_vida_monstruo;
    }
    public boolean get_existe(){
        return existe;
    }

    /*Nombre: combate
    Como parametros recibe un Tipo Jugador que corresponde al jugador
    Repite un ciclo donde se atacan ambas partes por partes partiendo por el jugador hasta que alguno quede sin vida
    Dependiendo de quien quede sin vida se imprimen distintos mensajes
    */
    String attack;
    public void combate(Jugador player) {
        if(status_vida_monstruo){    
            System.out.println("De repente, un monstruo aparece");
            System.out.println(player.get_nombre() + ": Te derrotare rufian y ya no atormentaras estas tierras");
            int dano_jugador;
            while (player.get_vida() > 0 && vida > 0){
                System.out.print("Quieres hacer un ataque o un hechizo?: ");
                attack = Main.entrada.nextLine();
                if (attack.equals("ataque")){
                    dano_jugador = player.ataque();
                    System.out.println(player.get_nombre() + ": ataca cuerpo a cuerpo al monstruo inflingiendo " + dano_jugador + " puntos de dano");
                    vida -= dano_jugador;
                } else {
                    dano_jugador = player.hechizo();
                    System.out.println(player.get_nombre() + ": ataca con un hechizo a inflingiendo " + dano_jugador + " puntos de dano");
                    vida -= dano_jugador;
                }
                if (vida > 0){
                    System.out.println("Monstruo: ¿A eso llamas un ataque? Eres re noob pibe");
                    System.out.println("El monstruo ataca a " + player.get_nombre() + " inflingiendo " + dano + " puntos de dano");
                    player.set_vida(player.get_vida()-dano);
                }
            }
            if (vida <= 0){
                System.out.println(player.get_nombre() + ": Ya no atormentaras a estas tierras");
                status_vida_monstruo = false;
                for (int i = 0; i < player.get_lista_misiones().size(); i++){
                    if (Character.compare(player.get_lista_misiones().get(i).get_requisito(), 'm') == 0){ //necesito hacerlo asi para poder dar las recompensas de la mision
                        player.get_lista_misiones().get(i).set_cantidad(player.get_lista_misiones().get(i).get_cantidad()+1);
                    } 
                }
            } else {
                System.out.println(player.get_nombre() + " a muerto a manos del monstruo");
                player.set_vida(0);
            }
        } else {
            System.out.println(player.get_nombre() + ": Parece que el monstruo de estas tierras ya a sido derrotado anteriormente, por mi por supuesto");
        }
    }
}
