#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <sys/types.h>
#include <string.h>
#include <sys/stat.h>
#include <stdbool.h>

  
/*
Nombre: mover_archivo
---------------------
Parametros:
    char *nombre_archivo: puntero char que corresponde al nombre del archivo a mover
    char *nombre_directorio: puntero char que corresponde al nombre del directorio al que se movera el archivo
---------------------
Descripcion:
    Esta funcion mueve un archivo a un directorio especificado
    No retorna nada
*/
int mover_archivo(char *nombre_archivo, char *nombre_directorio){
    char *nueva_direccion = malloc(strlen(nombre_directorio) + strlen(nombre_archivo) + 2);
    sprintf(nueva_direccion, "%s/%s", nombre_directorio, nombre_archivo);
    int result = rename(nombre_archivo, nueva_direccion);
    free(nueva_direccion);
    return result;
    }

struct txt{
    char *linea1;
    char *linea2;
    char *linea3;
};

/*
Nombre: save
---------------------
Parametros:
    char *nombre: puntero char que corresponde al nombre del archivo
---------------------
Descripcion:
    Esta funcion extrae la informacion de un archivo txt y la guarda en un struct
    Retorna un struct con la informacion del archivo
*/
struct txt *save(char *nombre){
    char *linea = NULL;
    size_t len = 0;
    ssize_t read;
    FILE *fp = fopen(nombre, "r");
    int i = 0;
    struct txt *file = malloc(sizeof(struct txt));
    while ((read = getline(&linea, &len, fp)) != -1) {
        if(i == 0){
            file->linea1 = malloc(sizeof(char) * strlen(linea));
            strcpy(file->linea1, linea);
        }
        else if(i == 1){
            file->linea2 = malloc(sizeof(char) * strlen(linea));
            strcpy(file->linea2, linea);
        }
        else if(i == 2){
            file->linea3 = malloc(sizeof(char) * strlen(linea));
            strcpy(file->linea3, linea);
        }
        i++;
    }
    fclose(fp);
    return file;
}


/*
Nombre: crear
---------------------
Parametros:
    char *nombre: puntero char que corresponde al nombre del genero del videojuego
---------------------
Descripcion:
    Esta funcion itera en las lineas de los archivos hasta la ultima linea
    Retorna un puntero char con el nombre del directorio
*/

 char *crear(char *nombre){
     char *linea = NULL;
     size_t len = 0;
     ssize_t read;
     FILE *fp = fopen(nombre, "r");
     while ((read = getline(&linea, &len, fp)) != -1) {
     }
     fclose(fp);
     return linea;
 }



int main(int argc, char *argv[]){

    int opcion;
    printf("Ingrese 1 ordenar por Cantidad_Actual o 2 para ordenar por Mayor_Cantidad: ");
    scanf("%d", &opcion);
    

    
    DIR *d;
    struct dirent *dir;
    d = opendir(".");
    if (d){
        while ((dir = readdir(d)) != NULL){
            if (strstr(dir->d_name, ".txt")){
                char *nombre = dir->d_name;
                char *c_genero = crear(nombre);
                char *genero = save(nombre)->linea3;
                char *genero2 = save(nombre)->linea3;
                char *genero3 = save(nombre)->linea3;

                int j_actuales= atoi(save(nombre)->linea1);
                int mayor_jugadores= atoi(save(nombre)->linea2);

                char *sc_40 = strcat(genero, "/Menor_a_40000");
                char *sc_40_80 = strcat(genero2, "/Entre_40000_y_80000");
                char *sc_80 = strcat(genero3, "/Mayor_a_80000");
                mkdir(c_genero, 0777);
                mkdir(sc_40, 0777);
                mkdir(sc_40_80, 0777);
                mkdir(sc_80, 0777);
                /*si opcion es igual a 1 ordenar por j_Actuales*/
                if (opcion == 1){
                    if (j_actuales < 40000){
                        mover_archivo(nombre, sc_40);
                    }
                    else if (j_actuales >= 40000 && j_actuales <= 80000){
                        mover_archivo(nombre, sc_40_80);
                    }
                    else if (j_actuales > 80000){
                        mover_archivo(nombre, sc_80);
                    }
                }
                /*si opcion es igual a 2 ordenar por mayor_jugadores*/
                else if (opcion == 2){
                    if (mayor_jugadores < 40000){
                        mover_archivo(nombre, sc_40);
                    }
                    else if (mayor_jugadores >= 40000 && mayor_jugadores <= 80000){
                        mover_archivo(nombre, sc_40_80);
                    }
                    else if (mayor_jugadores > 80000){
                        mover_archivo(nombre, sc_80);
                    }
                }
            }
        }
        closedir(d);
    }
    return(0);
}
