package game;

public class Mision {
    private char requisito; //v o m dependiendo de la mision
    private int valor; //coordenada de la casilla que se quiere llegar o cantidad de mounstruos que se tiene que matar
    private int cantidad; //posicion actual o cantidad matada actual osea lo que lleva el jugador
    private int recompensa; //xp por cumplir la mision
    private boolean status_mision;

    public Mision(char requisito, int valor, int recompensa){
        this.requisito = requisito;
        this.valor = valor;
        cantidad = 0;
        this.recompensa = recompensa;
    }

    public void set_requisito(char requisito){ //SETTERS
        this.requisito = requisito;
    }
    public void set_valor(int valor){
        this.valor = valor;
    }
    public void set_cantidad(int cantidad){
        this.cantidad = cantidad;

    }
    public void set_recompensa(int recompensa){
        this.recompensa = recompensa;
    }
    public void set_status_mision(boolean status_mision){
        this.status_mision = status_mision;
    }

    public char get_requisito(){
        return requisito;
    }
    public int get_valor(){
        return valor;
    }
    public int get_cantidad(){
        return cantidad;
    }
    public int get_recompensa(){
        return recompensa;
    }
    public boolean get_status_mision(){
        return status_mision;
    }

    public boolean verificar_requisito(){ //retorna true si la completo, false si no
        if (status_mision){
            return true;
        }
        return false;
    }
}
