#include <iostream>
#include <fstream>
#include <string>
#include <cstring>

using namespace std;

struct FlujoNeto {
	int hora;    //valores de 0 a 23
	int minuto;   //valores de 0 a 59
	int personas; //diferencia de personas
};

struct empleados{ //creamos un struct para ordenar nuestros datos, aprovechamos de separar horas y minutos para futuras comparaciones
	string estado;
	string rut;
	int hin;
	int min;
	bool chequeado;	
};




int cantidadPersonas (string hora){  //la funcion toma el string recibido como parametro y lo divide en 2 variables, de tipo string para 										   posteriormente covertirlas en variables tipo entero. Lee el archivo "flujo.publico.dat" y con condicionales 										   que verifican que la hora del registro siendo leido sea menor a la hora dada en el parametro y va sumando 										   la diferencia de personas en la variable "cant_actual". Finalmente, retorna esta variable "cant_actual".   										   
	FlujoNeto pt;
	
	string heure = hora.substr(0,2) , minute = hora.substr(3,4); // toma el string hora dado como parametro y lo divide en 																		2 strings, heure almacena los dos primeros caracteres que corresponden a las 																	    horas y minute almacena los ultimos 2 caracteres que corresponden a los 																    minutos.
	
	int hora_parametro = stoi(heure);	//inicializa una variable tipo entero que corresponde a la variable heure convertida a entero.
	int min_parametro = stoi(minute);	//inicializa una variable tipo entero que corresponde a la variable minute convertida a entero.
	int cant_actual = 0; 			//indica la cantidad de personas a la hora solicitada		
			
	fstream fp; //nombre de la variable del archivo "flujo-publico.dat"

	
	fp.open("flujo-publico.dat", ios::in|ios::binary);
	
	if(!fp.is_open()) { //chequea si el archivo se abrió correctamente
			cerr << "Error al abrir el archivo" << endl;
			exit (1);
		}
		
	while (fp.read((char*)&pt, sizeof(FlujoNeto))) { //lee el archivo "flujo-publico.dat" linea por linea
				
		if (hora_parametro > pt.hora) { //verifica que la hora leida sea mas temprano que la hora dada en el parametro
			cant_actual += pt.personas; //suma la diferencia de personas a la variable cant_personas 
		}
		else if (hora_parametro == pt.hora && min_parametro >= pt.minuto){ //verifica que los minutos sean mas tempranos que los minutos dados en 																				 el parametro
			cant_actual += pt.personas; //suma la diferencia de personas a la variable cant_personas 
		};
		
	
	}; 
	fp.close();		
	
	
	
		//huellero
	string hhtest, mmtest;
	hhtest = hora.substr(0,2);
	mmtest = hora.substr(3,4);
	int htest = stoi(hhtest);
	int mtest = stoi(mmtest);
	int N, i;
	int personasenlocal = 0, contlineas = 0;
	fstream fq;
	fq.open("asistencia.txt", ios::in);
	
	if(!fq.is_open()) {
		cerr << "error al abrir archivo" << endl;
		exit(1);
	}
	char c;
	int AUX = 0; 
	string es, rut, heu;
	
	while (fq >> es >> rut >> heu){ //obtener datos desde el txt
		
		if (es == "S" || es == "E"){ // esta 1era lectura del archivo solo se usa para obtener el numero de lineas y asi crear un arreglo del largo necesario
			contlineas++;
		}
		
	}
	fq.close();
	
	fstream fm;
	fm.open("asistencia.txt", ios::in);
	
	if(!fm.is_open()) {
		cerr << "error al abrir archivo" << endl;
		exit(1);
	}
	
	N = contlineas;	
	empleados emp[N];
	int x= 0;
	string  eos, run, heur;
	while (fm >> eos >>  run >> heur){
	
		emp[x].estado = eos;
		emp[x].rut = run;
		emp[x].hin= stoi(heur.substr(0,2));
		emp[x].min= stoi(heur.substr(3,5));
		emp[x].chequeado = 0;
		x++;
	}	
	string r;
	string est;
	for(int i=0; i<N; i++){
 		r = emp[i].rut; // guardamos el rut a comparar para usarlo en el siguiente for
 		est= emp[i].estado;
 		int hh = emp[i].hin;
 		int mm = emp[i].min;
 		if( hh < htest || hh == htest && mm <= mtest){
 		
 			if(emp[i].chequeado == 0){
 				
 				if (est == "E"){ // solo toma las entradas para compararlas, asumiendo que si un empleado salio primero tuvo que entrar
 				personasenlocal++;
 				
	 				for(int f=i+1; f<N; f++){ //i+1 para que no se compare con sigo mismo
	 					int hf = emp[f].hin;
	 					int mf = emp[f].min;
	 					
	 					if( hf < htest || hf == htest && mf <= mtest){
		 					if (r == emp[f].rut && emp[f].chequeado == 0){
		 						if (est == emp[f].estado){
		 							emp[f].chequeado = 1;
		 						
		 						}else{
		 							personasenlocal--;
		 							emp[f].chequeado = 0;
		 						}	
		 					
		 					}
	 					}
	 				}
 				}
 				
 			}
 		}
	
	}
	
	fm.close();
	
	cout << "cant_actual " << cant_actual << endl;
	cout << "personasenlocal " << personasenlocal << endl;
	
	cant_actual += personasenlocal;
	
	return cant_actual;	
}

int main () {
	string hora;
	cout << "hora: ";
	cin >> hora;
	cout << "cantidad de wns es: " << cantidadPersonas(hora) << endl;
}
