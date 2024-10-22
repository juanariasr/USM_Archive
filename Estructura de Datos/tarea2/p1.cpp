#include <iostream>
#include <fstream>
#include <string>
#include <cstring>

struct pol{
	int id; //numero del polinomio
	int exp; // exponente del monomio
	int coef; //coeficiente del monomio
	int tam; //tamaño del polinomio
	pol* sig;
}

class tLista {
	private:
		tNodo* head;
		tNodo* tail;
		tNodo* curr;
		unsigned int listSize;
		unsigned int pos; //posicion actual en la lista
	public: //metodos de la clase
		void clear(); //borra todos los elementos de la lista, reiniciandola como vacia

		int insert(tElemLista item); //inserta un elemento en la posicion actual de la lista

		int append(tElemLista item); //agrega un elemento al final de la lista

		tElemLista erase(); //borra el elemento actual y retorna su valor

			//manipuladores del cursor
		void moveToStart(); //mueve la posicion actual al comienzo de la lista

		void moveToEnd(); //mueve la pos. actual al final del la lista

		void next(); // mueve la posicion actual al siguiente elemento en la lista, si se esta en la cola no porduce cambios

		void prev(); //mueve la posicion actual al elemento anterior, no produce cambios si se esta en la cabeza de la lista

			//operaciones extra
		int lenght(); //retorna el numero de elemntos

		int currPos(); //retorna la posicion del elemento actual

		void moveToPos(int pos); //mueve a la posicion actual especificada

		tElemLista getValue(); //obtiene el valor del elemento actual de la lista
}


void evaluar(int i, float x){
	fstream fq;
	string cant; //indica la cantidad de polinomios del archivo
	fq.open("entradaPolinomio.txt", ios::in);
	
	if(!fq.is_open()) {
		cerr << "error al abrir archivo" << endl;
		exit(1);
	}
	
	getline(fq, cant) //se saca el entero N en formato string corresponidiente a la cantidad de polinomios del archivo
	
	int n; //contador de polinomios
	
	while (n != i+1) {
		if (n == i)
			 
	
		n++;
	};
	fq.close();
}










