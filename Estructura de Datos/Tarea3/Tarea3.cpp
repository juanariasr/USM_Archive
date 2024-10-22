#include <iostream>
#include <fstream>
#include <math.h>
#include <string>
#include <string.h>
#define VACIA -1 //Definimos qué es una clave vacía

using namespace std;


//Definimos lo que es un producto
struct producto {
    int cod_producto;
    char nombre_producto[31];
    int precio;
};

//Definimos lo que es una oferta
struct oferta {
    int cod_producto;
    int cantidad_descuento;
    int descuento;
    int productos_equivalentes[10];
};

//Definimos lo que es un contador de ofertas
struct contadorO {
    int cod_producto; //Código del producto principal de la oferta
    int productosComprados; //Productos comprados actualmente de la oferta
};

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
    int digitos_sobrantes = DigNum - cuantosDig + 1;
    return stoi(strNum.substr((digitos_sobrantes/2)-1,cuantosDig));

}

//Copia todos los elementos del segundo array en el primero
void arrcpy(int a1[],int a2[],int tamanio){for(int i=0;i<tamanio;i++){a1[i] = a2[i];}}


/* Definiciones de funciones compartidas */

//Función h, de parámetros tiene la clave y el tamaño de la tabla de hashing
int h(int clave, int M){

    int digM = cuantos_digitos(M);  //Obtenemos los dígitos del tamaño de nuestra tabla de hashing

    clave = clave*clave; //Elevamos nuestra clave al cuadrado

    int digitos_centrales = digCen(clave,digM); //Obtenemos los dígitos centrales de la clave

    return (digitos_centrales%M); //Retornamos asegurándonos de que el número esté dentro de la tabla
    
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

//Inserta un producto en nuestro hashing de productos, recibe de parámetros el arreglo que sirve de tabla, el tamaño de este y el producto a insertar
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

//Inserta una oferta en nuestro hashing de ofertas, recibe de parámetros el arreglo que sirve de tabla, el tamaño de este y la oferta a insertar
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
oferta hashSearchO(oferta TablaO[], int clave, int M) {

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
    return false; //Se retorna false indicando que no se encontró el contador

    
}


int main(){

    //Abrimos los archivos binarios

    ifstream fileP,fileO;
    fileP.open("productos.dat",ios::binary);
    fileO.open("ofertas.dat",ios::binary);

    //Vigilamos que se hayan abierto adecuadamente

    if (!fileP.is_open()){cout << "Problema al abrir el archivo de productos" << endl; exit(1); }
    if (!fileO.is_open()){cout << "Problema al abrir el archivo de ofertas" << endl; exit(1); }

    //Almacenamos la cantidad de structs de cada uno

    int cantP; //Cantidad de productos en el archivo de productos
    int cantO; //Cantidad de ofertas en el archivo de ofertas

    fileP.read((char *)&cantP, sizeof(int)); //Le damos el valor correspondiente a cantP
    fileO.read((char *)&cantO, sizeof(int)); //Le damos el valor correspondiente a cantO

    //Inicializamos los Arrays

    int largeP = round(cantP/0.7)+1; //Obtengo el largo que debe tener nuestra tabla de productos mediante regla de 3 (la cantidad de productos debería ser su 70%)
    int largeO = round(cantO/0.7)+1; //Obtengo el largo que debe tener nuestra tabla de ofertas mediante regla de 3 (la cantidad de ofertas debería ser su 70%)

    producto TablaP[largeP]; //Declaro el arreglo de productos que usaremos de tabla de hashing
    oferta TablaO[largeO]; //Declaro el arreglo de ofertas que usaremos de tabla de hashing
    contadorO TablaCO[largeO]; //Declaro el arreglo de contadores de ofertas que usaremos de tabla de hashing

    inicializarP(TablaP,largeP); //Inicializamos el array de productos
    inicializarO(TablaO,largeO); //Inicializamos el array de ofertas
    inicializarCO(TablaCO,largeO); //Inicializamos el array de contadores de ofertas

    //Ir insertando los productos

    bool hubo_repetidas = false; //Definimos una variable booleana para avisar si hay productos repetidos en el archivo

    for(int i = 0 ; i < cantP ; i++){
        producto prod; //Declaramos un struct producto
        fileP.read((char *)&prod, sizeof(producto)); //Almacenamos dentro de él uno de los productos del archivo
        int comprobante = hashInsertP(TablaP, prod, largeP); //Insertamos el producto en nuestra tabla de hashing y definimos un comprobante que nos diga si se insertó o no
        if (hubo_repetidas == false && comprobante == 0) hubo_repetidas = true; //Si nuestro comprobante nos dice que no se insertó y todavía no se repetía, se avisa
    }

    if (hubo_repetidas == true) cout << "Hubo claves repetidas, favor de arreglar archivo de productos" << endl; //Si en algún momento se repitió, se manda el mensaje

    //Ir insertando las ofertas y los contadores de ofertas

    hubo_repetidas = false; //Devolvemos a la variable hubo_repetidas a su valor falso para que siga cumpliendo su trabajo

    for(int i = 0 ; i < cantO ; i++){
        oferta ofer; //Declaramos un struct oferta
        contadorO count; //Declaramos un struct contador de ofertas
        fileO.read((char *)&ofer, sizeof(oferta)); //Almacenamos dentro de él una de las ofertas del archivo
        count.cod_producto = ofer.cod_producto; //Almacenamos el código de la oferta en el contador de ofertas
        count.productosComprados = 0; //Inicializamos el contador
        int comprobante = hashInsertO(TablaO, ofer, largeO); //Insertamos la oferta en nuestra tabla de hashing y definimos un comprobante que nos diga si se insertó o no
        hashInsertCO(TablaCO,count,largeO); //Insertamos el contador en nuestra tabla de hashing
        if (hubo_repetidas == false && comprobante == 0) hubo_repetidas = true; //Si nuestro comprobante nos dice que no se insertó y todavía no se repetía, se avisa
    }

    if (hubo_repetidas == true) cout << "Hubo claves repetidas, favor de arreglar archivo de ofertas" << endl; //Si en algún momento se repitió, se manda el mensaje

    //Cerramos los archivos ya que no los vamos a necesitar más
    fileP.close();
    fileO.close();

    //Abrimos el archivo de texto para leer
    fstream fileText;
    fileText.open("compras.txt", ios::in);

    //Vigilamos que se haya abierto correctamente
    if( !fileText.is_open() ){cout << "Error al abrir el archivo de texto\n"; exit(1);}

    //Almacenamos la información de a cuántos clientes hay que atender
    string clientesS;
    getline(fileText,clientesS);
    int clientes = stoi(clientesS);

    //Creamos el archivo de salida
    fstream fileSalida;
    fileSalida.open("boletas.txt", ios::out);

    //Vigilamos que se haya abierto correctamente
    if( !fileSalida.is_open() ){cout << "Error al crear el archivo de boletas\n"; exit(1);}

    //Escribimos cuántas boletas vamos a escribir
    fileSalida << clientes << endl;

    //Iniciamos el ciclo for para ir cliente por cliente
    for(int i = 0 ; i<clientes ; i++){

        //Declaramos la variable principal coste
        int coste = 0;

        //Leemos la cantidad de productos del cliente
        string productosS;
        getline(fileText,productosS);
        int productos = stoi(productosS);

        //Iniciamos un ciclo for para ir producto por producto
        for(int e = 0 ; e<productos ; e++){

            //Leemos el producto
            string IDproductoS;
            getline(fileText,IDproductoS);
            int IDproducto = stoi(IDproductoS);

            //Buscamos en nuestra tabla de hashing de qué producto se trata
            producto prod;
            prod = hashSearchP(TablaP,IDproducto,largeP);

            //Revisamos si no se trata de un producto inexistente
            if(prod.cod_producto == -1){cout << "Se incluyó en el archivo de texto un producto inexistente, favor de arreglar el problema.\n"; exit(1);}

            //Agregamos su precio al coste total de esta boleta
            coste += prod.precio;

            //Buscamos la oferta correspondiente a este producto
            oferta ofer;
            ofer = hashSearchO(TablaO,IDproducto,largeO);

            //Declaramos nuestra variable de búsqueda, que nos servirá para darnos cuenta cuando debemos dejar de buscar
            bool seEncontro = false; //Declaramos una variable booleana para indicar si se encontró un producto equivalente que ya hubiera pasado por caja

            //Se evalúa si alguno de sus productos equivalentes ya fue pasado por caja
            for(int a = 0 ; a<10 && ofer.productos_equivalentes[a] != -1 && seEncontro == false ; a++){

                //Buscamos y almacenamos el contador del producto equivalente actual
                contadorO contadorActual = hashSearchCO(TablaCO,ofer.productos_equivalentes[a],largeO);
                
                cout << a << endl;

                //Evaluamos si el producto equivalente pasó o no por caja
                if (contadorActual.productosComprados > 0){
                    //Si lo hizo avisamos de que se encontró y le sumamos un producto al contador de la oferta
                    seEncontro = true;
                    hashPlusCO(TablaCO,ofer.productos_equivalentes[a],largeO);
                }
            }

            //Si ningún producto equivalente fue pasado por caja anteriormente
            if (seEncontro == false) hashPlusCO(TablaCO,IDproducto,largeO); //Se aumenta en 1 el contador de oferta de la oferta con el ID del producto actual
        }

        //Evaluamos uno por uno cada contador de oferta y descontamos según sea debido
        for (int u = 0 ; u<largeO ; u++){
            //Para todo contador de ofertas que tenga un producto o más en su haber
            if (TablaCO[u].cod_producto != -1 && TablaCO[u].productosComprados > 0){
                oferta ofer = hashSearchO(TablaO,TablaCO[u].cod_producto,largeO); //Se busca su oferta
                int descuento; //Se declara una variable de descuento
                int cuantos_descuentos = (TablaCO[u].productosComprados/ofer.cantidad_descuento); //Se calcula por cuanto multiplicar el descuento
                descuento = ofer.descuento*cuantos_descuentos; //Se calcula el descuento
                coste -= descuento; //Y se aplica al coste total de la boleta
            }
        }

        //Escribimos el coste resultante en el archivo de salida
        fileSalida << coste << endl;
    }

    //Aquí deberían cerrarse los archivos
    fileText.close();
    fileSalida.close();

    return 0;
}

//Declaramos la función h que nos ayudará a insertar y buscar los registros
int h(int clave, int M);

//Declaramos la función h2 que nos ayudará a insertar y buscar los registros
int h2(int clave);

//Declaramos la función p que nos ayudará a insertar y buscar los registros
int p(int clave, int intento);

//Declaramos la función de inicializar el hashing de productos (lo incializa con todas las claves vacías)
void inicializarP(producto TablaP[], int tamanio);

//Declaramos la función de inicializar el hashing de ofertas (lo inicializa con todas las claves vacías)
void inicializarO(oferta TablaO[], int tamanio);

//Declaramos la función de inicializar el hashing de contadores de ofertas (lo inicializa con todas las claves vacías)
void inicializarCO(contadorO TablaP[], int tamanio);

//Declaramos la función hashInsertP, que servirá para insertar un producto, sus parámetros son el arreglo de nuestra tabla, el producto a insertar y el tamaño del arreglo
int hashInsertP(producto TablaP[] , producto prod, int M);

//Declaramos la función hashInsertO, que servirá para insertar una oferta, sus parámetros son el arreglo de nuestra tabla, la oferta a insertar y el tamaño del arreglo
int hashInsertO(oferta TablaO[], oferta ofer, int M);

//Declaramos la función hashInsertCO, que servirá para insertar un contador de ofertas, sus parámetros son el arreglo de nuestra tabla, el contador de ofertas a insertar y el tamaño del arreglo
int hashInsertCO(contadorO TablaCO[], contadorO count, int M);

//Declaramos la función hashSeachP, que servirá para buscar un producto, sus parámetros son el arreglo de nuestra tabla, la clave y el tamaño del arreglo
producto hashSearchP(producto TablaP[], int clave, int M);

//Declaramos la función hashSeachO, que servirá para buscar una oferta, sus parámetros son el arreglo de nuestra tabla, la clave y el tamaño del arreglo
oferta hashSearchO(oferta TablaO[], int clave, int M);

//Declaramos la función hashSeachCO, que servirá para buscar un contador, sus parámetros son el arreglo de nuestra tabla, la clave y el tamaño del arreglo
contadorO hashSearchCO(contadorO TablaCO[], int clave, int M);

//Declaramos la función hashPlusCO, que servirá para buscar un contador y aumentarlo en 1, sus parámetros son el arreglo de nuestra tabla, la clave y el tamaño del arreglo
bool hashPlusCO(contadorO TablaCO[], int clave, int M);

//Declaramos la función es_par que te dice si un número es par
bool es_par(int n);

//Declaramos la función cuantos_digitos que te dice cuántos dígitos tiene un número
int cuantos_digitos(int n);

//Declaramos digCen que te indica los dígitos centrales de un número, toma como parámetros un número y los dígitos que se quieren conservar de este
int digCen(int num, int cuantosDig);

//Declaramos arrcpy que copia todos los elementos del segundo array en el primero
void arrcpy(int a1[],int a2[],int tamanio);
