package tutorialpoo;

public class Furgoneta extends Coche{ //ahora la clase furgoneta es una subclase y la clase coche es una superclase
    private int capacidad_carga;
    private int plazas_extra;

    public Furgoneta(int plazas_extra, int capacidad_carga){
        super(capacidad_carga); //llama al constructor de la clase padre o sea coche

        this.capacidad_carga = capacidad_carga;

        this.plazas_extra = plazas_extra;
     }
     public String get_datosFurgoneta(){
         return "La capacidad de carga es: " + capacidad_carga + " y las placzas son: " + plazas_extra;
     }
}
