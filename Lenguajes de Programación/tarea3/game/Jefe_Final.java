package game;


public class Jefe_Final implements Enemigos{
    private String nombre;
    private int vida;
    private int dano_base;
    private boolean status_combate;

    /*Nombre: Jefe_Final
    Como parametros recibe un String nombre que es el nombre del jefe final y dos enteros que corresponden a la vida y al daño base del jefe final respectivamente
    Constructor*/
    public Jefe_Final(String nombre, int vida, int dano_base){
        this.nombre = nombre;
        this.vida = vida;
        this.dano_base = dano_base;
        status_combate = false;
    }
    //SETTERS de la clase Jefe_Final
    public void set_nombre(String nombre){
        this.nombre = nombre;
    }
    public void set_vida(int vida){ 
        this.vida = vida;
    }
    public void set_dano_base(int dano){
        this.dano_base= dano;
    }
    public void set_statu_combate(boolean status_combate){
        this.status_combate = status_combate;
    }
    //GETTERS de la clase Jefe_Final
    public String get_nombre(){
        return nombre;
    }
    public int get_vida(){ 
        return vida;
    }
    public int get_dano_base(){
        return dano_base;
    }
    public boolean get_status_combate(){
        return status_combate;
    }

    /*Nombre: combate
    Como parametros recibe un Tipo Jugador que corresponde al jugador
    Primero guarda una variable con la vida inicial del jefe que sera util para saber en que fase esta dicho jefe
    Luego repite un ciclo donde se atacan ambas partes por partes partiendo por el jugador hasta que alguno quede sin vida
    Si el jugador quedo sin vida imprime algunos mensajes junto al 'Game Over'
    Si el jefe final quedo sin vida imprime un mensaje y actualiza el valor de status a true
    */
    public void combate(Jugador player) {
        int vida_inicial = vida;
        System.out.println(player.get_nombre() + ": wowowowow me estoy enfrentando a " + nombre + " el jefe final mas op del momento");
        System.out.println(get_nombre() + ": Asi es papu y soy la ultima cosa que jamas veras");
        while (player.get_vida() > 0 && vida > 0){
            System.out.print("Quieres atacar con un ataque o un hechizo?: ");
            String attack = Main.entrada.nextLine();
            int dano_jugador;
            if (vida <= vida_inicial/50){
                System.out.println("El jefe final esta en fase 1");
                if (attack.equals("ataque")){
                    dano_jugador = player.ataque();
                    System.out.println(player.get_nombre() + " ataca cuerpo a cuerpo a " + nombre + " inflingiendo " + dano_jugador + " puntos de dano");
                    vida -= dano_jugador;
                } else {
                    dano_jugador = player.hechizo();
                    System.out.println(player.get_nombre() + " ataca con un hechizo a " + nombre + " inflingiendo " + dano_jugador + " puntos de dano");
                    vida -= dano_jugador;
                }
                
                if (vida > 0){
                    System.out.println(get_nombre() + ": Re malardo, ahora si te viene una");
                    System.out.println(get_nombre() + " ataca a " + player.get_nombre() + " inflingiendo " + (dano_base+2) + " puntos de dano");
                    player.set_vida(player.get_vida()-(dano_base+2));
                }
            } else {
                System.out.println("El jefe final esta en fase 2");
                if (attack.equals("ataque")){
                    dano_jugador = player.ataque();
                    System.out.println(player.get_nombre() + " ataca cuerpo a cuerpo a " + nombre + " inflingiendo " + dano_jugador + " puntos de dano");
                    vida -= dano_jugador;
                } else {
                    dano_jugador = player.hechizo();
                    System.out.println(player.get_nombre() + " ataca con un hechizo a " + nombre + " inflingiendo " + dano_jugador + " puntos de dano");
                    vida -= dano_jugador;
                }
                
                if (vida > 0){
                    System.out.println(get_nombre() + ": Re malardo, ahora si te la ganastes");
                    System.out.println(nombre + " ataca a " + player.get_nombre() + " inflingiendo " + (dano_base+4) + " puntos de dano");
                    player.set_vida(player.get_vida()-(dano_base+4));
                }
            }
            System.out.println(" ");
        }
        if (vida <= 0){
            System.out.println("AAA soy el mas cracks de los cracks, mate al jefe llamado " + nombre);
            status_combate = true;
        } else {
            System.out.println(get_nombre() + ": Yo sabia que no tendrias chance contra mi");
            System.out.println(player.get_nombre() + " a muerto a manos de " + get_nombre());
            System.out.println("Game Over");
        }
        
        
    }

    
}
