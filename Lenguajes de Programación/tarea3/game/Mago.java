package game;

class Mago extends Jugador{
    /*Nombre: Mago
    Como parametros recibe un String nombre que es el nombre del jugador 
    Actualiza las estadisticas del jugador generico a las especificas del tipo guerrero
    Constructor*/
    public Mago(String nom) {
        super(nom);
        set_max_vida(10);
        set_max_energia(6);
        set_max_mana(15);
        set_vida(10); //MAX 10
        set_fuerza(3);
        set_inteligencia(10);
        set_energia(6); //MAX 6
        set_mana(15); //MAX 15
    }

    /*Nombre: ataque
    Primero verifica si el jugador tiene suficiente energia para realizar el ataque, en caso de que no tenga retorna 0
    Si se tiene suficiente energia se hacen los calculos para ver el valor del ataque y se retorna el valor del ataque
    */
    public int ataque(){
        if(get_energia() == 0){
            System.out.println(get_nombre() + ": Maldicion no tengo energia para atacar");
            return 0;
        }
        int melee_damage = (get_fuerza() * Math.round(get_inteligencia()/4)) + get_energia();
        set_energia(get_energia()-3);
        if(get_energia()-3 < 0){
            System.out.println(get_nombre() + ": Rayos y centellas parece que me quede sin energia tras ese ataque");
            return 0;
        }
        return melee_damage;
    /*Nombre: hechizo
    Primero verifica si el jugador tiene suficiente mana para realizar el hechizo, en caso de que no tenga retorna 0
    Si se tiene suficiente mana se hacen los calculos para ver el valor del hechizo y se retorna el valor del hechizo
    */
    }
    public int hechizo(){
        if(get_mana() == 0){
            System.out.println(get_nombre() + ": Maldicion no tengo mana para hacer el hechizo");
            return 0;
        }
        int spell_damage = (get_inteligencia() * Math.round(get_fuerza()/4)) + get_mana();
        set_energia(get_mana()-5);
        if(get_mana()-5 < 0){
            System.out.println(get_nombre() + ": Rayos y centellas parece que me quede sin mana tras ese hechizo");
            return 0;
        }
        return spell_damage;
    }

    /*Nombre: subir_experiencia
    Como parametro recibe un entero correspondiente a la cantidad de experiencia ganada
    Primero actualiza la cantidad de experiencia del jugador, y guarda en la variable level_actual el valor de el nivel actual del jugador
    posteriormente actualiza el nivel del jugador y compara si el nivel nuevo y el nivel anterior son diferentes
    si son diferentes significa que el jugador subio de nivel por lo que hace los calculos necesarios para subir las estadisticas del mismo
    */
    public void subir_experiencia(int xp_ganada) {
        System.out.println(get_nombre() + ": OH SI!, gane xp");
        set_xp(get_xp() + xp_ganada);
        int level_actual = get_nivel_actual();
        set_nivel_actual(get_xp());
        int nuevo_level_actual = get_nivel_actual();
        if (nuevo_level_actual != level_actual){
            System.out.println(get_nombre() + ": Wowow! subi de nivel " + level_actual + " a nivel " + nuevo_level_actual);
        }
        while (nuevo_level_actual != level_actual){
            set_max_vida(get_max_vida() + 2*nuevo_level_actual);
            set_fuerza(get_fuerza() + 1);
            set_inteligencia(get_inteligencia() + 3*nuevo_level_actual);
            set_max_energia(get_max_energia()+1);
            set_max_mana(get_max_mana()+3*nuevo_level_actual);
            set_vida(get_max_vida());
            set_energia(get_max_energia());
            set_mana(get_max_mana());
            nuevo_level_actual -= 1;
            
        }
        System.out.println(get_nombre() + ": Lo que significa que mis estadisticas quedaron de la siguiente forma: ");
        System.out.println("La vida de " + get_nombre() + " es " + get_vida());
        System.out.println("La cantidad de xp de " + get_nombre() + " es " + get_xp());
        System.out.println("La fuerza de " + get_nombre() + " es " + get_fuerza());
        System.out.println("La inteligencia de " + get_nombre() + " es " + get_inteligencia());
        System.out.println("La energia de " + get_nombre() + " es " + get_energia());
        System.out.println("El mana de " + get_nombre() + " es " + get_mana());
    }
}
