vendedor* vendeProducto(string filename, int cod /*codigo del producto*/, int k, int& size /*tamaño del arreglo retornado*/) {
	fstream fp;
	
	fp.open(filename, ios::in|ios::binary);
	
	if(!fp.is_open()) {
			cerr << "Error al abrir el archivo" << endl;
			return 1;
		}
	
	int n; //entero que guardara el numero de structs vendedor
	fp.read((char*)&n, sizeof(int));
	
	vendedor* X = new vendedor [n]; 
	
	fp.read((char*)X, n*sizeof(int));
	
	fp.close();
	
		//tengo que filtrar a todos los vendedores que hayan vendido el producto dado en el parametro
	
	vendedor* vendedores = new vendedor [size]; //arreglo de vendedores a retornar
	int f = 0; //cursor de arreglo vendedores
	
	for (int i=0; i<n; i++) { 							//recorriendo X
		int c = 0; /*contador total de ventas*/											//cantidad total del producto vendido
		for (int u=0 ; u < X[i].n_ventas; u++){			//recorriendo transaccion por vendedor
			if (X[i].ventas[u].codigo_prod == cod) { 		 //si el codigo es el solitiado
				c += X[i].ventas[u].cantidad;
			};
		};
		if (c >= k) {							 //si la cantidad total de ventas es mayor que k
			vendedores[f] = X[i]; 				//añade el vendedor al arreglo vendedores
			f++;
		};
			
	}; 	
	
	size = f+1;						//tamaño del arreglo retornado
	
	delete[] X;
	
	return vendedores;
}
