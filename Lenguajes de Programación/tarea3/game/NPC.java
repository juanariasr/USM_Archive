package game;


abstract class NPC {
    private String nombre;

    /*Nombre: NPC
    Como parametros recibe un string con el nombre del npc
    Constructor*/
    public NPC(String nombre){
        this.nombre = nombre;
    }

    
    //SETTERS de la clase NPC
    public void set_nombre(String nombre){
        this.nombre = nombre;
    }
    //GETTERS de la clase NPC
    public String get_nombre(){ 
        return nombre;
    }

    public abstract void interaccion(Jugador player);
}
