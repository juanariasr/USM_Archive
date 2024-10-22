1
6
1
1
2
2
3
1//Estas funciones deben incluírse en el código de la tarea3 cuando vaya a entregarse

#include <string>
#include <string.h>
#define VACIA -1 //Definimos qué es una clave vacía

using namespace std;

/* Definiciones de estructuras */

//Definimos lo que es un producto
struct producto {
    int cod_producto; //Tiene un código
    char nombre_producto[31]; //Un nombre
    int precio; //Y un precio
};

//Definimos lo que es una oferta
struct oferta {
    int cod_producto; //Tiene un código hacia el producto que representa
    int cantidad_descuento; //Una cantidad de productos definida para aplicar un descuento
    int descuento; //Un descuento
    int productos_equivalentes[10]; //Y un máximo de 10 productos equivalentes
};

//Definimos lo que es un contador de ofertas
struct contadorO {
    int cod_producto; //Código del producto principal de la oferta
    int productosComprados; //Productos comprados actualmente de la oferta
};


/* Definiciones de funciones compartidas */

//Función h, de parámetros tiene la clave y el tamaño de la tabla de hashing
int h(int clave, int M){

    int contador = 1; //Definimos nuestro contador de dígitos y lo inicializamos en 1

    int digM = cuantos_digitos(M);  //Obtenemos los dígitos del tamaño de nuestra tabla de hashing

    clave = clave*clave; //Elevamos nuestra clave al cuadrado

    int dígitos_centrales = digCen(clave,digM); //Obtenemos los dígitos centrales de la clave

    return (dígitos_centrales%M); //Retornamos asegurándonos de que el número esté dentro de la tabla
    
}

//Función h2, tiene la clave de parámetro, suma a la clave 4 y luego la multiplica por sí misma
int h2(int clave){clave = (clave + 4)*clave; return clave;}

//Función p, tiene la clave y el número de intento de parámetros, retorna el intento multiplicado por la función h2 aplicada a la clave
int p(int clave, int intento){return intento*h2(clave);}


/* Definiciones de funciones especilizadas para el hashing de PRODUCTOS */

//Inicializa nuestro hashing de productos mediante un arreglo que servirá de tabla y el tamaño de ese arreglo
void inicializarP(producto TablaP[], int tamanio){
    
    producto prod; //Declaramos un producto
    
    prod.cod_producto = VACIA; //Inicializamos el código del producto como vacío
    
    for (int i = 0 ; i < tamanio ; i++) TablaP[i] = prod; //Copiamos nuestro producto en todas las posiciones del arreglo

}

//Inserta un producto en nuestro hashing de productos, recibe de parámetros el arreglo que sirve de tabla, el tamaño de esta y el producto a insertar
int hashInsertP(producto TablaP[], producto prod, int M) {

    int inicio, pos; //Declaramos las variables de inicio y posición

    pos = inicio = h(prod.cod_producto, M); //Las inicializamos en la posición que nos dicte nuestra función h

    //Iniciamos un ciclo for que se detendrá cuando encontremos una posición vacía o nos demos cuenta que la clave se repitió
    for (int i = 1; TablaP[pos].cod_producto != VACIA && TablaP[pos].cod_producto != prod.cod_producto; i++) 

        pos = (inicio + p(prod.cod_producto, i)) % M; //Actualizamos posición hasta la próxima ranura en la secuencia

    if (TablaP[pos].cod_producto == prod.cod_producto) return 0; // inserción no exitosa: clave repetida

    else {

        TablaP[pos].cod_producto = prod.cod_producto; //Se guarda el valor del código del producto
        strcpy(TablaP[pos].nombre_producto,prod.nombre_producto); //Se guarda el valor del nombre del producto
        TablaP[pos].precio = prod.precio; //Se guerda el valor del precio del producto
        return 1; // inserción exitosa

    }
}

//Busca y retorna el producto asociado a una clave específica, toma como parámetros esta clave, el arreglo en el que basamos nuestra tabla de hashing y su tamaño
producto hashSearchP(producto TablaP[], int clave, int M) {

    int inicio, pos; //Declaramos las variables de inicio y posición

    pos = inicio = h(clave, M); //Las inicializamos en la posición que nos dicte nuestra función h

    //Iniciamos un ciclo for que se detendrá cuando encontremos una posición vacía o encontremos la clave
    for (int i = 1; TablaP[pos].cod_producto != VACIA && TablaP[pos].cod_producto != clave; i++) 

        pos = (inicio + p(clave, i)) % M; //Actualizamos posición hasta la próxima ranura en la secuencia

    if (TablaP[pos].cod_producto == clave) return TablaP[pos]; //Si encontramos la clave devolvemos el producto que esta nos indica

    //De lo contrario
    else {
        producto prod; //Declaramos un producto
        prod.cod_producto = -1; //Le otorgamos una clave vacía
        return prod; //Retornamos el producto
    }
}


/* Definiciones de funciones especilizadas para el hashing de OFERTAS */

//Inicializa nuestro hashing de ofertas mediante un arreglo que servirá de tabla y el tamaño de ese arreglo
void inicializarO(oferta TablaO[], int tamanio){

    oferta ofer;

    ofer.cod_producto = VACIA;

    for (int i = 0 ; i < tamanio ; i++) TablaO[i] = ofer;

}

int hashInsertO(oferta TablaO[], oferta ofer, int M) {

    int inicio, pos; //Declaramos las variables de inicio y posición

    pos = inicio = h(ofer.cod_producto, M); //Las inicializamos en la posición que nos dicte nuestra función h

    //Iniciamos un ciclo for que se detendrá cuando encontremos una posición vacía o nos demos cuenta que la clave se repitió
    for (int i = 1; TablaO[pos].cod_producto != VACIA && TablaO[pos].cod_producto != ofer.cod_producto; i++) 

        pos = (inicio + p(ofer.cod_producto, i)) % M; //Actualizamos posición hasta la próxima ranura en la secuencia

    if (TablaO[pos].cod_producto == ofer.cod_producto) return 0; //inserción no exitosa: clave repetida

    else {

        TablaO[pos].cantidad_descuento = ofer.cantidad_descuento; //Se guarda el valor de la cantidad de productos hasta el descuento
        TablaO[pos].cod_producto = ofer.cod_producto; //Se guarda el valor del código del producto al que se aplica la oferta
        TablaO[pos].descuento = ofer.descuento; //Se guarda el valor del descuento
        arrcpy(TablaO[pos].productos_equivalentes,ofer.productos_equivalentes,10); //Se guarda el valor de los productos equivalentes
        return 1; // inserción exitosa
    }
}

//Busca y retorna la oferta asociada a una clave específica, toma como parámetros esta clave, el arreglo en el que basamos nuestra tabla de hashing y su tamaño
oferta hashSearchP(oferta TablaO[], int clave, int M) {

    int inicio, pos; //Declaramos las variables de inicio y posición
    
    pos = inicio = h(clave, M); //Las inicializamos en la posición que nos dicte nuestra función h

    //Iniciamos un ciclo for que se detendrá cuando encontremos una posición vacía o encontremos la clave
    for (int i = 1; TablaO[pos].cod_producto != VACIA && TablaO[pos].cod_producto != clave; i++) 

        pos = (inicio + p(clave, i)) % M; //Actualizamos posición hasta la próxima ranura en la secuencia

    if (TablaO[pos].cod_producto == clave) return TablaO[pos]; //Si encontramos la clave devolvemos el producto que esta nos indica

    //De lo contrario
    else {

        oferta ofer; //Declaramos una oferta
        ofer.cod_producto = -1; //Le otorgamos una clave vacía
        return ofer; //Retornamos la oferta

    }
}

/* Definiciones de funciones especilizadas para el hashing de CONTADORES DE OFERTAS */

//Inicializa nuestro hashing de contadores de ofertas mediante un arreglo que servirá de tabla y el tamaño de ese arreglo
void inicializarCO(contadorO TablaP[], int tamanio){
    
    contadorO count; //Declaramos un contador
    
    count.cod_producto = VACIA; //Inicializamos el código del contador como vacío

    count.productosComprados = 0; //Inicializamos el contador de productos comprados en 0
    
    for (int i = 0 ; i < tamanio ; i++) TablaP[i] = count; //Copiamos nuestro contador en todas las posiciones del arreglo

}

//Inserta un contador en nuestro hashing de productos, recibe de parámetros el arreglo que sirve de tabla, el tamaño de esta y el contador a insertar
int hashInsertCO(contadorO TablaCO[], contadorO count, int M) {

    int inicio, pos; //Declaramos las variables de inicio y posición

    pos = inicio = h(count.cod_producto, M); //Las inicializamos en la posición que nos dicte nuestra función h

    //Iniciamos un ciclo for que se detendrá cuando encontremos una posición vacía o nos demos cuenta que la clave se repitió
    for (int i = 1; TablaCO[pos].cod_producto != VACIA && TablaCO[pos].cod_producto != count.cod_producto; i++) 

        pos = (inicio + p(count.cod_producto, i)) % M; //Actualizamos posición hasta la próxima ranura en la secuencia

    if (TablaCO[pos].cod_producto == count.cod_producto) return 0; // inserción no exitosa: clave repetida

    else {

        TablaCO[pos].cod_producto = count.cod_producto; //Se guarda el valor del código del contador de la oferta
        TablaCO[pos].productosComprados = count.productosComprados; //Se inicializa el contador de productos comprados
        return 1; // inserción exitosa

    }
}

//Busca y retorna el contador asociado a una clave específica, toma como parámetros esta clave, el arreglo en el que basamos nuestra tabla de hashing y su tamaño
contadorO hashSearchCO(contadorO TablaCO[], int clave, int M) {

    int inicio, pos; //Declaramos las variables de inicio y posición

    pos = inicio = h(clave, M); //Las inicializamos en la posición que nos dicte nuestra función h

    //Iniciamos un ciclo for que se detendrá cuando encontremos una posición vacía o encontremos la clave
    for (int i = 1; TablaCO[pos].cod_producto != VACIA && TablaCO[pos].cod_producto != clave; i++) 

        pos = (inicio + p(clave, i)) % M; //Actualizamos posición hasta la próxima ranura en la secuencia

    if (TablaCO[pos].cod_producto == clave) return TablaCO[pos]; //Si encontramos la clave devolvemos el contador que esta nos indica

    //De lo contrario
    else {
        contadorO count; //Declaramos un contador
        count.cod_producto = -1; //Le otorgamos una clave vacía
        return count; //Retornamos el contador
    }
}

//Sirve para aumentar en 1 un contador específico, los parámetros son el arrat de contadores, la clave del contador a aumentar y el tamaño del array
bool hashPlusCO(contadorO TablaCO[], int clave, int M){
    int inicio, pos; //Declaramos las variables de inicio y posición

    pos = inicio = h(clave, M); //Las inicializamos en la posición que nos dicte nuestra función h

    //Iniciamos un ciclo for que se detendrá cuando encontremos una posición vacía o encontremos la clave
    for (int i = 1; TablaCO[pos].cod_producto != VACIA && TablaCO[pos].cod_producto != clave; i++) 

        pos = (inicio + p(clave, i)) % M; //Actualizamos posición hasta la próxima ranura en la secuencia

    //Si encontramos el contador
    if (TablaCO[pos].cod_producto == clave) {
        TablaCO[pos].productosComprados+=1; //Aumentamos en 1 el contador
        return true; //Retornamos true para indicar que el contador se encontró y se aumentó
    }

    //De lo contrario
    else {return false;} //Se retorna false indicando que no se encontró el contador
}


/* Definiciones de funciones simplificadoras */

//Te dice si un número es par
bool es_par(int n){

    if (n%2 == 0) return true; //Si el resto al dividir por 2 es 0, se retorna verdad

    else return false; //Si no lo es, se retorna mentira

}

//Te dice cuántos dígitos tiene un número
int cuantos_digitos(int n){

    int contador = 1; //Se inicia el contador de dígitos en 1

    //Mientras el número no llegue a tener 1 solo dígito exacto
    while(n/10 > 0){
        n = n/10; //Le quitaremos al número uno de sus dígitos
        contador++; //Y el contador contará un dígito más
    }

    return contador; //Retornamos el contador de dígitos

}

//Te indica los dígitos centrales de un número, toma como parámetros un número y los dígitos que se quieren conservar de este
int digCen(int num, int cuantosDig){

    int DigNum = cuantos_digitos(num); //Almacena en la variable DigNum los dígitos del número

    if (cuantosDig > DigNum) return num; //Si se quieren conservar todos los dígitos del número se retorna el número completo

    string strNum = to_string(num); //Se convierte el número a un string

    //Si la paridad de los dígitos del número y de los dígitos que se quieren conservar de este es equivalente
    if (es_par(DigNum) == es_par(cuantosDig)) {
        int digitos_sobrantes = DigNum - cuantosDig; //Se toman como dígitos que sobran los dígitos del número menos los dígitos que queremos conservar
        return stoi(strNum.substr(digitos_sobrantes/2,cuantosDig)); //Se retorna un sub string que se salta la mitad de los dígitos sobrantes y tiene tamaño cuantosDig
    }

    //Si la paridad de los dígitos de un número y de los dígitos que se quieren conservar es diferente 
    else if(es_par(DigNum) != es_par(cuantosDig)) {
        int digitos_sobrantes = DigNum - cuantosDig + 1;
        return stoi(strNum.substr((digitos_sobrantes/2)-1,cuantosDig));
    }

}

//Copia todos los elementos del segundo array en el primero
void arrcpy(int a1[],int a2[],int tamanio){for(int i=0;i<tamanio;i++){a1[i] = a2[i];}}
