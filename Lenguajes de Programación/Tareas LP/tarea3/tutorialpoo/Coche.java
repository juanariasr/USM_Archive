package tutorialpoo;

public class Coche{ //lo que va a hacer este poo es e tipico caso del auto
        private int ruedas; //estos ints van a ser globales para todos los metodos y clases
        private int largo;
        private int ancho;
        private int motor;
        private int peso_plataforma;
        private String color;
        private int peso_total;
        private boolean asientos_cuero, climatizador;

        public Coche(int ruedas){ //Este es el constructor de la clase, el cual debe tener el public y el mismo nombre que la clase
            this.ruedas = ruedas;
            largo = 2000;
            ancho = 300;
            motor = 1600;
            peso_plataforma = 500;
        }
        public String get_largo(){ //GETTERS, necesitan return
            return "El largo del carro es " + largo;
        }
        public int get_ruedas(){
            return ruedas;
        }
        public int get_ancho(){
            return ancho;
        }
        public int get_motor(){
            return motor;
        }
        
        public String get_color(){
            return "El color del carro es: " + color;
        }
        public int get_pesoTotal(){
            return peso_total;
        }
        public String get_asientos(){
            if(asientos_cuero == true){
                return "La nae tiene asientos de cuero";
            }else{
                return "La nae NO tiene asientos de cuero";
            }
        }
        public String get_climatizador(){
            if(climatizador == true){
                return "El carro tiene climatizador";
            }else {
                return "El carro NO tiene climatizador";
            }
        }
        public int get_precio_coche(){ 
            int precio_final = 10000;
            if (asientos_cuero == true){
                precio_final += 2000;
            }
            if (climatizador == true){
                precio_final += 1500;
            }
            return precio_final;
        }

        public String get_datos_generales(){
            return "La plataforma del vehiculo tiene " + ruedas + " ruedas. Mide " + largo/1000 + " metros con un ancho de " + ancho + " cm y un peso de plataforma de " + peso_plataforma + " kg";
        }

        public void set_color(String color_coche){ //SETTERS, no necesitan return
            color = color_coche;
        }
        public void set_asientos(String asientos_cuero){ //el metodo this se usa cuando un parametro tiene el mismo nombre que una variable private
            if (asientos_cuero == "si"){
                this.asientos_cuero = true;
            }else{
                this.asientos_cuero = false;
            }
        }
        public void set_climatizador(String climatizador){
            if(climatizador == "si"){
                this.climatizador = true;
            } else{
                this.climatizador = false;
            }
        }
        
        public String get_peso(){//SETTER Y GETTER AL MISMO TIEMPO
            int peso_carroceria = 500; //esta variable solo es visible dentro del metodo
            peso_total = peso_plataforma + peso_carroceria;
            if(asientos_cuero == true){
                peso_total += 50;
            }
            if(climatizador == true){
                peso_total += 20;
            }
            return "El peso del coche es " + peso_total;
        }

        
    }
