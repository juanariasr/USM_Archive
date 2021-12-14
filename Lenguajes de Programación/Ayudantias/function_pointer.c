#include "stdio.h"

int suma(int a, int b){
    return a + b;
}

int main(){
    int (*puntero_funcion)(int,int); //tipo_a_retornar (*variable_puntero) (par1,par2,...,par_n)
    puntero_funcion = &suma;
    int x = 3;
    int y = 4;
    printf("La suma de %d + %d es: %d\n",x,y,puntero_funcion(x,y));
    return 0;
}