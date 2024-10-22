#include <iostream>
#include <fstream>

using namespace std;

int main() {
	ofstream fp;
	int i = 5;
	fp.open("archivo.dat", ios::binary);
	if (!fp.is_open()) {
		cerr << "Error el abrir el archivo" << endl;
		return 1; //error
	}
	
	fp.write((char*)&i, sizeof(int)); //escribe el valor de i en el archivo
	
	fp.close();
	return 0;
}
