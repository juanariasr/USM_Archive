package game;

public abstract class Tierra {
    private float probabilidad_enemigo;
    private Monstruos monstruo;
    private Jefe_Final jefe_final;
    private NPC npc;

    /*Nombre: Tierra
    Como parametros recibe un flotante que corresponde a la probabilidad de que el monstruo aparezca, 
    un tipo Monstruo que corresponde al monstruo que puede haber en esta tierra, Un tipo Jefe_Final que corresponde al jefe final que puede haber en esta tierra,
    Un tipo NPC que corresponde al npc que puede estar en esta tierra
    Constructor*/
    public Tierra(float probabilidad_enemigo, Monstruos monstruo, Jefe_Final jefe_final, NPC npc){
        this.probabilidad_enemigo = probabilidad_enemigo;
        this.monstruo = monstruo;
        this.jefe_final = jefe_final;
        this.npc = npc;
    }
    //SETTERS de la clase Tierra
    public void set_probabilidad_enemigo(float probabilidad){//SETTERS
        probabilidad_enemigo = probabilidad;
    }
    public void set_monstruo(Monstruos monstruo){
        this.monstruo = monstruo;
    }
    public void set_jefe_final(Jefe_Final jefe_final){
        this.jefe_final = jefe_final;
    }
    public void set_npc(NPC npc){
        this.npc = npc;
    }
    //GETTERS de la clase Tierra
    public float get_probabilidad_enemigo(){ //GETTERS
        return probabilidad_enemigo;
    }
    public Monstruos get_monstruo(){
        return monstruo;
    }
    public Jefe_Final get_jefe_final(){
        return jefe_final;
    }
    public NPC get_npc(){
        return npc;
    }

    public abstract boolean accion(Jugador player);
}
