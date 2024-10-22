#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>

#define cant_cartas 44
#define n_filas 4
#define l_filas 5


typedef struct {
  int valor;
  int puntaje;
}Carta;

typedef struct {
    int puntos;
    Carta mano[10];
    int turno;
    int largo;
    int player;
}Jugador;


typedef struct {
  int *cartas;
  int largo;
}Fila;

typedef struct {
  Carta *cartas[44];
  int largo;
}Mazo;

//funciones

/*
rellenar_mazo:
Mazo *mazo: recibe el mazo a rellenar
Funcion rellena un mazo con las cartas del 1 al 44.
*/
void rellenar_mazo(Mazo* mazo) {
    int valor = 1;
    int indice = 0;
    for (int i = 0; i < 44; i++) {
        Carta carta;
        carta.valor = valor;
        if (valor % 11 == 0) {
            carta.puntaje = 5;
        } else if (valor % 10 == 0) {
            carta.puntaje = 3;
        } else if (valor % 5 == 0) {
            carta.puntaje = 2;
        } else {
            carta.puntaje = 1;
        }
        mazo->cartas[indice] = malloc(sizeof(Carta));
        *(mazo->cartas[indice]) = carta;
        indice++;
        valor++;
    }
    mazo->largo = indice;
}

/*
repartir_cartas_filas:
Mazo *mazo: recibe el mazo a repartir
Fila *filas: recibe las filas a rellenar
Funcion reparte a cada fila 1 carta del mazo.
*/
void repartir_cartas_filas(Mazo* mazo, Fila* filas) {
  for (int i = 0; i < 4; i++) {
    filas[i].cartas = (int*) malloc(sizeof(int));
    filas[i].largo = 1;
    filas[i].cartas[0] = mazo->cartas[mazo->largo-1]->valor;
    mazo->largo--;
    
  }
}


/*
repartir_cartas_jugadores:

Mazo *mazo: recibe el mazo a repartir
Jugador *jugadores: recibe los jugadores a los cuales les debe repartir las cartas

Funcion reparte a cada jugador 10 cartas del mazo.

*/
void repartir_cartas_jugadores(Mazo* mazo, Jugador* jugadores) {
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < jugadores->largo; j++) {
            jugadores[i].mano[j] = *(mazo->cartas[mazo->largo-1]);
            mazo->largo--;
        }
    }
}

/*
barajar_mazo:

Mazo *mazo: recibe el mazo a barajar

Funcion baraja el mazo de forma aleatoria.

*/
void barajar_mazo(Mazo* mazo) {
    srand(time(NULL));
    int i, j;
    Carta temp;
    for (i = 0; i < mazo->largo; i++) {
        j = rand() % mazo->largo;
        temp = *(mazo->cartas[i]);
        *(mazo->cartas[i]) = *(mazo->cartas[j]);
        *(mazo->cartas[j]) = temp;
    }
}

/*
imprimir_filas:

Fila *filas: recibe las filas a imprimir
int num_filas: recibe la cantidad de filas existentes

Funcion imprime las filas con sus respectivas ultimas cartas y ademas su largo.

*/

void imprimir_filas(Fila* filas, int num_filas) {
    for (int i = 0; i < num_filas; i++) {
        printf("Fila %d: ", i);
        printf("%d \n", filas[i].cartas[filas[i].largo-1]);
        printf("\nLa cantidad de cartas de la fila es %d\n", filas[i].largo);
    }
    
}

/*
imprimir_mano_jugador:

Jugador *jugador: recibe el jugador a imprimir sus cartas

Funcion imprime la mano del jugador.

*/

void imprimir_mano_jugador(Jugador* jugador) {
    printf("Mano del jugador %d: ", jugador->player);
    for (int i = 0; i < jugador->largo; i++) {
        printf(" %d", jugador->mano[i].valor);
    }
    printf("\n");
}

/*
ordenar_mano:

Jugador *jugador: recibe el jugador a ordenar sus cartas en mano

Funcion ordena la mano del jugador de menor a mayor.

*/

void ordenar_mano(Jugador *jugador) {
    int i, j;
    Carta temp;
    int n = sizeof(jugador->mano) / sizeof(Carta);

    for (i = 0; i < n-1; i++) {
        for (j = 0; j < n-i-1; j++) {
            if (jugador->mano[j].valor > jugador->mano[j+1].valor) {
                temp = jugador->mano[j];
                jugador->mano[j] = jugador->mano[j+1];
                jugador->mano[j+1] = temp;
            }
        }
    }
}

/*
asignar_turnos:

Jugador *jugadores: recibe los jugadores a los cuales se les asignara un turno

Funcion asigna los turnos a cada jugador de forma ascendente de acuerdo a la carta mas baja de su mano.

*/
void asignar_turnos(Jugador* jugadores) {
    int orden_jugadores[4] = {0, 1, 2, 3};
    for (int i = 0; i < 3; i++) {
        for (int j = i + 1; j < 4; j++) {
            if (jugadores[orden_jugadores[i]].mano[0].valor > jugadores[orden_jugadores[j]].mano[0].valor) {
                int temp = orden_jugadores[i];
                orden_jugadores[i] = orden_jugadores[j];
                orden_jugadores[j] = temp;
            }
        }
    }
    Jugador temp_jugadores[4];
    for (int i = 0; i < 4; i++) {
        temp_jugadores[i] = jugadores[orden_jugadores[i]];
        temp_jugadores[i].turno = i + 1;
    }
    for (int i = 0; i < 4; i++) {
        jugadores[i] = temp_jugadores[i];
    }
}



/*
poner_en_fila_jugador:

Fila *filas: recibe la fila a la cual se le pondra una carta
Jugador *jugador: recibe el jugador que pondra la carta
int n_fila: recibe el numero de la fila a la cual se le pondra la carta
int n_carta: recibe el indice de la carta que se pondra en la fila

*/
void poner_en_fila_jugador(Fila* filas, Jugador* jugador, int n_fila, int n_carta) {
    verificar_fila(filas, jugador);
    printf("%d",jugador->mano[n_carta].valor);
    printf("%d",filas->cartas[filas->largo-1]);
    filas->cartas[filas->largo] = jugador->mano[n_carta].valor;
    filas->largo++;
    for (int i = n_carta; i < jugador->largo-1; i++) {
        jugador->mano[i] = jugador->mano[i+1];
        printf("%d",jugador->mano[i].valor);
    }
    jugador->largo--;
}


/*
poner_carta_bot:

Fila *fila: recibe la fila a la cual se le pondra una carta
Jugador *jugador: recibe el bot que pondra la carta

funcion que pone una carta del bot en la fila que recibe como parametro

*/
void poner_carta_bot(Fila* fila, Jugador* jugador){
    for (int i = 0; i < jugador->largo; i++) {
        if (jugador->mano[i].valor > fila->cartas[fila->largo-1]) {
            poner_en_fila_jugador(fila, jugador, fila->largo-1, i);
            return;
        } 
    }
    poner_en_fila_jugador(fila, jugador, fila->largo-1, 0);
}

/*

verificar_fila:

Fila *fila: recibe la fila a la cual se verificara si se le puede colocar la carta
Jugador *jugador: recibe el jugador al cual se le verificaran las cartas

funcion que verifica si se le puede colocar una carta a la fila, si se le puede colocar, coloca la carta, si no
se lleva la fila y se le asignan puntos al jugador correspondiente a las cartas 



*/

void verificar_fila(Fila* fila, Jugador* jugador) {
    if (fila->cartas[fila->largo - 1] > jugador->mano[jugador->largo-1].valor){
        for (int i = 0; i < fila->largo; i++) {
            if (fila->cartas[i] % 11 == 0) {
                jugador->puntos += 5;
            } else if (fila->cartas[i] % 10 == 0) {
                jugador->puntos += 3;
            } else if (fila->cartas[i] % 5 == 0) {
                jugador->puntos += 2;
            } else {
                jugador->puntos += 1;
            }
        }
        fila->largo = 0;
    }
    else if (fila->largo >= 5){
        for (int i = 0; i < 5; i++) {
            if (fila->cartas[i] % 11 == 0) {
                jugador->puntos += 5;
            } else if (fila->cartas[i] % 10 == 0) {
                jugador->puntos += 3;
            } else if (fila->cartas[i] % 5 == 0) {
                jugador->puntos += 2;
            } else {
                jugador->puntos += 1;
            }
        }
        fila->largo = 0;
        
    }
}


int main(){
    Jugador jugadores[4];

    for (int i = 0; i < 4; i++) {
        jugadores[i].largo = 10;
        jugadores[i].puntos = 0;
    }
    
    jugadores[0].player = 1; //nosotros somos este
    jugadores[1].player = 2; //bot
    jugadores[2].player = 3; //bot 2
    jugadores[3].player = 4; //bot 3

    

    

    Fila filas[n_filas];
    Mazo mazo;
    rellenar_mazo(&mazo);
    barajar_mazo(&mazo);
    repartir_cartas_filas(&mazo, &filas);
    repartir_cartas_jugadores(&mazo, &jugadores);
    printf("Cartas en filas:\n");
    imprimir_filas(&filas, n_filas);
    printf("____________________________________________________\n\n");

    for (int i = 0; i < 4; i++) {
        ordenar_mano(&jugadores[i]);
    }
    

    int n_fila, n_carta;
    int i = 0;
    
    while (i < 10){
        printf("turno %d\n", i+1);
        printf("---------------------------------------------\n");
        asignar_turnos(jugadores);
        for (int j = 0; j < 4; j++) {
            if (jugadores[j].player == 1) {
                imprimir_mano_jugador(&jugadores[j]);
                imprimir_filas(filas, n_filas);
                printf("ingrese numero de fila: ");
                scanf("%d", &n_fila);
                printf("ingrese indice de la carta: ");
                scanf("%d", &n_carta);
                poner_en_fila_jugador(&filas[n_fila], &jugadores[j], n_fila ,n_carta);
                printf("\n");
                fflush(stdin);
                fflush(stdout); 
            } else {
                int aleatorio = rand() % 4;
                printf("numero de fila bot: %d\n", aleatorio);
                imprimir_mano_jugador(&jugadores[j]);
                imprimir_filas(filas, n_filas);
                poner_carta_bot(&filas[aleatorio], &jugadores[j]);
                printf("\n");    
            }
            printf("---------------------------------------------\n");

        }

        
        i++;
    }
    int max = 0;
    int id;
    for (int i = 0; i < 4; i++) {
        if (jugadores[i].puntos > max) {
            max = jugadores[i].puntos;
            id = i;
            }
        }
    printf("El ganador es el jugador %d con %d puntos\n", jugadores[id].player, jugadores[id].puntos);
   return 0;
}