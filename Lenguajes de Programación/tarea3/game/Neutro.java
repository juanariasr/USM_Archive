package game;

public class Neutro extends NPC {
    private char requisito;
    private int valor;
    private int recompensa;
    private boolean ya_dio_mision;

    /*Nombre: Neutro
    Como parametros recibe un String nombre que es el nombre del npc, un caracter que corresponde al requisito que el jugador tendra que completar
    un entero valor que corresponde a el valor que el jugador tendra que llegar para cumplir el requisito
    y un entero recompensa que sera la cantidad de xp que el npc le dara al jugador por cumplir el requisito
    Constructor*/
    public Neutro(String nombre, char requisito, int valor, int recompensa){
        super(nombre);
        this.requisito = requisito;
        this.valor = valor;
        this.recompensa = recompensa;
        ya_dio_mision = false;
    }

    /*Nombre: set_requisito
    Como parametros recibe caracter requisito que sera el valor que se le asignara a la variable del mismo nombre
    */
    public void set_requisito(char requisito){ //SETTERS
        this.requisito = requisito;
    }
    /*Nombre: set_valor
    Como parametros recibe entero valor que sera el valor que se le asignara a la variable del mismo nombre
    */
    public void set_valor(int valor){
        this.valor = valor;
    }
    /*Nombre: set_recompensa
    Como parametros recibe entero recompensa que sera el valor que se le asignara a la variable del mismo nombre
    */
    public void set_recompensa(int recompensa){
        this.recompensa = recompensa;
    }
    /*Nombre: set_ya_dio_mision
    Como parametros recibe booleano status que sera el valor que se le asignara a la variable ya_dio_mision
    */
    public void set_ya_dio_mision(boolean status){
        ya_dio_mision = status;
    }

    /*Nombre: get_requisito
    Retorna el valor de la variable requisito
    */
    public char get_requisito(){ //GETTERS
        return requisito;
    }
    /*Nombre: get_valor
    Retorna el valor de la variable valor
    */
    public int get_valor(){
        return valor;
    }
    /*Nombre: get_recompensa
    Retorna el valor de la variable recompensa
    */
    public int get_recompensa(){
        return recompensa;
    }
    /*Nombre: get_ya_dio_mision
    Retorna el valor de la variable ya_dio_mision
    */
    public boolean get_ya_dio_mision(){
        return ya_dio_mision;
    }

    /*Nombre: interaccion
    Primero verifica si el npc ya dio mision, luego dependiendo del requisito crea una variable mision con valores previamente establecidos por el DM
    Luego si el jugador acepta la mision la añade a la lista de misiones del jugador y se actualiza el valor de ya_dio_mision a true
    Si el npc ya habia dado mision previamente imprime un mensaje por pantalla y si el jugador rechaza la mision no se añade nada a la lista de misiones*/
    public void interaccion(Jugador player) {
        String answer;
        if (ya_dio_mision == false){
            if (requisito == 'v'){
                Mision mision  = new Mision(requisito, valor, recompensa);
                System.out.println(get_nombre() + ": Hello There, ¿Quieres cumplir esta mision? Deberas llegar a " + valor + " del mundo y recibiras " + recompensa + " de xp");
                System.out.print("Introduce tu respuesta(si/no): ");
                answer = Main.entrada.nextLine();
                if (answer.equals("si")){
                    System.out.println("Maravilloso, espero que la completes para darte tu xp");
                    player.add_to_list(mision);
                    set_ya_dio_mision(true);
                }
            } else {
                Mision mision  = new Mision(requisito, valor, recompensa);
                System.out.println(get_nombre() + ": Hello There, ¿Quieres cumplir esta mision? Deberas matar a " + valor + " de monstruos y recibiras " + recompensa + " de xp.");
                System.out.print("Introduce tu respuesta(si/no): ");
                answer = Main.entrada.nextLine();
                if (answer.equals("si")){
                    System.out.println(get_nombre() + ": Maravilloso, espero que la completes para darte tu xp");
                    player.add_to_list(mision);
                    set_ya_dio_mision(true);
                }
            }
        } else {
            System.out.println(get_nombre() + ": Ya te di mi mision compa, saludos");
        }
    }

}
