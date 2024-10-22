#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <sys/types.h>
#include <string.h>
#include <sys/stat.h>
#include <stdbool.h>
#include <unistd.h>

int main(void){

    DIR *directory;
    struct dirent *entry;
    int orden;

    printf("Escoja el orden por el cual se ordeno los juegos: \n 1. Numero de jugadores actuales \n 2. Numero de jugadores maximos \n");
    scanf("%d", &orden);
    
    directory = opendir(".");
    int menor_a_40000 = 0;
    int entre = 0;
    int mayor_a_80000 = 0;

    while ((entry = readdir(directory)) != NULL){
        char copia[100];
        if (entry->d_type == DT_DIR && strcmp(entry->d_name, ".") != 0 && strcmp(entry->d_name, "..") != 0 && strcmp(entry->d_name, ".vscode") != 0 ) {
            printf("Cantidad de juegos de %s: \n", entry->d_name);
            
 
            DIR *directory2;
            struct dirent *entry2;

            strcpy(copia, entry->d_name);
            strcat(copia, "/");
            strcat(copia, "Menor_a_40000");
            int cuenta = 0;
            directory2 = opendir(copia);
            while((entry2 = readdir(directory2)) != NULL){
                if (entry2->d_type == DT_REG && strcmp(entry2->d_name, ".") != 0 && strcmp(entry2->d_name, "..") != 0 ) {
                    cuenta++;
                    menor_a_40000++;
                    }
                }

            if (orden == 1){
                printf("       Juegos con una cantidad de jugadores actuales menor a 40000: %d \n", cuenta);
            } else{
                printf("       Juegos con una mayor cantidad de jugadores menor a 40000: %d \n", cuenta);
            }

            strcpy(copia, entry->d_name);
            strcat(copia, "/");
            strcat(copia, "Entre_40000_y_80000");
            cuenta = 0;
            directory2 = opendir(copia);
            while((entry2 = readdir(directory2)) != NULL){
                if (entry2->d_type == DT_REG && strcmp(entry2->d_name, ".") != 0 && strcmp(entry2->d_name, "..") != 0 ) {
                    cuenta++;
                    entre++;
                    }
                }
            if (orden == 1){
                printf("       Juegos con una cantidad de jugadores actuales entre 40000 y 80000: %d \n", cuenta);
            } else{
                printf("       Juegos con una mayor cantidad de jugadores entre 40000 y 80000: %d \n", cuenta);
            }

            strcpy(copia, entry->d_name);
            strcat(copia, "/");
            strcat(copia, "Mayor_a_80000");
            cuenta = 0;
            directory2 = opendir(copia);
            while((entry2 = readdir(directory2)) != NULL){
                if (entry2->d_type == DT_REG && strcmp(entry2->d_name, ".") != 0 && strcmp(entry2->d_name, "..") != 0 ) {
                    cuenta++;
                    mayor_a_80000++;
                    }
                }
            if (orden == 1){
                printf("       Juegos con una cantidad de jugadores actuales mayor a 80000: %d \n", cuenta);
            } else{
                printf("       Juegos con una mayor cantidad de jugadores mayor a 80000: %d \n", cuenta);
            }
        
            
             closedir(directory2);
        }
        }
        printf("Del total de juegos: \n");
            if (orden == 1){
                printf("       Existen %d con una cantidad de jugadores actuales menor a 40000\n", menor_a_40000);
                printf("       Existen %d con una cantidad de jugadores actuales entre 40000 y 80000 \n", entre);
                printf("       Existen %d con una cantidad de jugadores actuales mayor a 80000 \n", mayor_a_80000);
            } else{
                printf("       Existen %d con una mayor cantidad de jugadores menor a 40000 \n", menor_a_40000);
                printf("       Existen %d con una mayor cantidad de jugadores entre 40000 y 80000 \n", entre);
                printf("       Existen %d con una mayor cantidad de jugadores mayor a 80000 \n", mayor_a_80000);
            }
    
        closedir(directory);
        
}