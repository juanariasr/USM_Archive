#include <iostream>
#include <fstream>
#include <string>
#include <cstring>

#include "tabb.hpp"

using namespace std;


int main(){
	fstream fm;
	fm.open("entradaPolinomio.txt", ios::in);
	int n, m, c_mon = 0;	
	if(!fm.is_open()) {
		cerr << "error al abrir archivo" << endl;
		exit(1);
	}
	fm >>n; //Tomamos la 1era liena del archivo que indica la cantidad de polinomios n y avanzamos 1 linea
	
	
	int raices[n]; //arreglo de raices


	cout << "cantidad de polinomios: " << n << endl;
	string exp, coef;
	for(int i = 0; i < n; i++){ //iteramos n veces para asegurarnos de guardar todos los polinomios
		fm >> m; //tomamos la cantidad de monomios m 
		 
		while (fm >> exp >> coef){
  			c_mon++;
  			
  			if(c_mon == m) {
				break;
			}
		}
		c_mon = 0;
		
	}
	string op, indice, xj, texto;
	//abrir archivo AUX
	
	fstream fp;
	
	fp.open("operaciones.txt", ios::out); //escribir en un archivo ASCII
	if(!fp.is_open()) {
		cerr << "Error al abrir el archivo" << endl;
		return 1;
	}
	
		
	while (fm >> op >> indice >> xj){ 	 //guarda las operaciones en un archivo auxiliar
		texto = op + " " + indice + " " + xj;
		fp << texto << endl;
	}
	
	fm.close();
	fp.close();
	
	cout << "checkpoint 1" << endl;
	
	fp.open("operaciones.txt", ios::in); //escribir en un archivo ASCII
	//fp.seekg(0)
	if(!fp.is_open()) {
		cerr << "Error al abrir el archivo" << endl;
		return 1;
	}
	
	while (fp >> op >> indice >> xj){ 	 //guarda las operaciones en un archivo auxiliar
		cout << "checkpoint 2" << endl;
		cout << op << " " << indice << " " << xj << endl;
		
		int indi = stof(indice);
		float _xj = stof(xj);
		fm.open("entradaPolinomio.txt", ios::in);
		if(!fm.is_open()) {
		cerr << "error al abrir archivo" << endl;
		exit(1);
		}	
		fm >> n; //Tomamos la 1era linea del archivo que indica la cantidad de polinomios n y avanzamos 1 linea

		cout << "cantidad de polinomios: " << n << endl;
		
		string exp, coef;
		
		for(int i = 0; i < n; i++){ //iteramos n veces para asegurarnos de guardar todos los polinomios
		cout << "evaluando polinomio: " << i << endl;
		
			fm >> m; //tomamos la cantidad de monomios m
			
			cout << "cantidad de monomios: " << m << endl;
			
			cout << endl;
			
			if (i == indi){ //si se llega al polinomio solicitado se empieza a trabajar con los monomios
			
				tABB tree; //arbol
				
				monomio nodo_requested;
				
				cout << "hurray encontraste el polinomio" << endl;
				tNodoArbolBin* mono = new tNodoArbolBin;
				while (fm >> exp >> coef){
	  		
		  			cout << "exp: " << exp << endl;
		  		
		  			cout << "coef: " << coef << endl;
		  			
		  			float expo = stof(exp);
		  			float coefi = stof(coef);
		  			
		  			
		  			
		  			mono -> info.exp = expo;
		  			
		  			mono -> info.coef = coefi;
		  			
		  			tree.insert(mono, nodo_requested, expo);
		  			
		  			c_mon++;
		  			
		  			if(c_mon == m) {
						break;
						}
					}
				c_mon = 0;
				
				if (op == "COEFICIENTE"){
					tree.inOrden(mono -> info.exp);
					//return nodo_requested.coef;  //se llama al TDA coeficiente en inorden el cual deberia hacer las weas q estan aca ahora
					//hacer weas de coef
					//se deberia imprimir el return
					}
				else if (op == "EVALUANDO") {
					//hacer weas de coeficiente
					//aplicar lo d horner q no se como es
					}
				}
				else {
				
					while (fm >> exp >> coef){
			  			c_mon++;
			  			
			  			if(c_mon == m) {
							break;
						}
					}
					c_mon = 0;
				}
			}
			fm.close();
		}
	return 0;
	}


