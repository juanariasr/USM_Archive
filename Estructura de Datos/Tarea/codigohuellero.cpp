#include<iostream>
#include<fstream>
#include<string>
#include<cstring>

using namespace std;

struct empleados{ //creamos un struct para ordenar nuestros datos, aprovechamos de separar horas y minutos para futuras comparaciones
	string estado;
	string rut;
	int hin;
	int min;
	bool chequeado;	
};




int main(){
	string hhtest, mmtest;
	hhtest = "13";
	mmtest = "30";
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
	string es, rut, heure;
	
	while (fq >> es >> rut >> heure){ //obtener datos desde el txt
		
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
		cout << emp[x].hin << " sape " << emp[x].min << endl;
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
	
	cout << personasenlocal << endl;
	return 0;
}
