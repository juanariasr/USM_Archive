package tutorialpoo;

//import javax.swing.*; este import sirve para hacer los inputs mas facil minuto 20 video 32 pildorasinformaticas

public class Uso_Vehiculo {
    public static void main(String [] args){
        /*Coche Renault = new Coche(); //instanciar una clase
        System.out.println(Renault.get_largo());

        Coche movil = new Coche();
        String colour;
        Scanner in = new Scanner(System.in);
        System.out.print("Introduzca color: ");
        colour = in.nextLine();
        movil.set_color(colour);
        System.out.println(movil.get_color());                  CODIGO DE LOS PRIMEROS VIDEOS CUANDO SE LLAMABA USO_COCHE
        in.close();

        movil.set_asientos("si");
        System.out.println(movil.get_asientos());

        movil.set_climatizador("si");
        System.out.println(movil.get_climatizador());

        System.out.println(movil.get_peso());

        System.out.println("El precio final del coche es " + movil.get_precio_coche());*/

        Coche micoche1 = new Coche(5);
        micoche1.set_color("Nagatoro");
        Furgoneta mifurgoneta1 = new Furgoneta(7, 420); //constructor de la clase que heredo de coche
        mifurgoneta1.set_color("Haiacchi");
        mifurgoneta1.set_asientos("Si");
        mifurgoneta1.set_climatizador("Si");
        System.out.println(micoche1.get_datos_generales() + ". " + micoche1.get_color());
        System.out.println(mifurgoneta1.get_datos_generales() + ". " + mifurgoneta1.get_datosFurgoneta());
    }
}
