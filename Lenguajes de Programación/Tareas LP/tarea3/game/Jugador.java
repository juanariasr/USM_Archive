package game;

import java.util.ArrayList;
import java.util.List;

public abstract class Jugador {
    private String nombre;
    private int vida;
    private int xp;
    private int fuerza;
    private int inteligencia;
    private int energia;
    private int mana;
    private List<Mision> lista_misiones;

    //Variables extras
    private int posicion_actual;
    private int nivel_actual;
    private int max_vida;
    private int max_energia;
    private int max_mana;
    
    /*Nombre: Jugador
    Como parametros recibe un String nombre que es el nombre del jugador
    Constructor*/
    public Jugador(String nom){
        nombre = nom;
        xp = 0;
        nivel_actual = 1;
        lista_misiones  = new ArrayList<Mision>();
    }

    //SETTERS de la clase jugador
    public void set_vida(int lp){ //SETTERS
        if (lp < max_vida){
            vida = lp; //LifePoints
        }else{
            vida = max_vida;
        }
    }
    
    public void set_xp(int xp){
        this.xp = xp; 
    }
   
    public void set_fuerza(int fuerza){
        this.fuerza = fuerza;
    }
    
    public void set_inteligencia(int inteligencia){
        this.inteligencia = inteligencia;
    }
    
    public void set_energia(int energia){
        if (energia < max_energia){
            this.energia = energia;
        }else{
            this.energia = max_energia;
        }
    }
    
    public void set_mana(int mana){
        if (mana < max_mana){
            this.mana = mana;
        }else{
            this.mana = max_mana;
        }
    }
    public void add_to_list(Mision mission){
        lista_misiones.add(mission);
    }
    public void set_posicion_actual(int posicion_actual){
        this.posicion_actual = posicion_actual;
    }
    
    public void set_nivel_actual(int xp){
        if (xp < 10){
            nivel_actual = 1;
        }else if (xp < 25){
            nivel_actual = 2;
        }else if (xp < 50){
            nivel_actual = 3;
        }else if (xp < 100){
            nivel_actual = 4;
        }else if (xp < 200){
            nivel_actual = 5;
        }else if (xp < 350){
            nivel_actual = 6;
        }else if (xp < 600){
            nivel_actual = 7;
        }else{
            nivel_actual = 8;
        }
    }
    public void set_max_vida(int max_vida){
        this.max_vida = max_vida;
    }
    public void set_max_energia(int max_energia){
        this.max_energia = max_energia;
    }
    public void set_max_mana(int max_mana){
        this.max_mana = max_mana;
    }

    //GETTERS de la clase jugador
    public String get_nombre(){ 
        return nombre;
    }
    public int get_vida(){
        return vida;
    }
    public int get_xp(){
        return xp;
    }
    public int get_fuerza(){
        return fuerza;
    }
    public int get_inteligencia(){
        return inteligencia;
    }
    public int get_energia(){
        return energia;
    }
    public int get_mana(){
        return mana;
    }
    public List<Mision> get_lista_misiones(){
        return lista_misiones;
    }
    public int get_posicion_actual(){
        return posicion_actual;
    }
    public int get_nivel_actual(){
        return nivel_actual;
    }
    public int get_max_vida(){
        return max_vida;
    }
    public int get_max_energia(){
        return max_energia;
    }
    public int get_max_mana(){
        return max_mana;
    }

    public abstract int ataque();

    public abstract int hechizo();

    public abstract void subir_experiencia(int xp_ganada);
}
