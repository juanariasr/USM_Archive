#include <iostream>
//cuando se pase un TDA como parametro mejir pasarlo por referencia

tPila merge(tPila A&, tPila B&) { //mejor pasarlas por referencia
	tPila C;
	tCola Q;
	
	while (B.size() > 0){ //saca los elementos de la pila descendiente y los pone en la cola
		Q.enqueue(B.topValue());
		B.pop();
	}
	
	while (Q.size() > 0){ //mete los elementos de la cola a la pila original pero esta vez los mete de manera ascendente
		B.push(Q.frontValue());
		Q.dequeue();
	}
	
	while (A.size() > 0 && B.size() > 0) { //va sacando los elementos de las pilas hasta que una se quede vacia
		if (A.topValue() < B.topValue()){
			C.push(A.topValue() );
			A.pop();
		} else {
			C. push( B.topValue() );
			B.pop();
		}
	}
	
	while (A.size() > 0){ //saca los elementos de la pila A si es que quedan
		C.push( A.topValue());
		A.pop();
	}
	
	while( B.size() > 0){
		C.push(B.topValue());
		B.pop();
	}
	return C;
}


	//segundo ejercicio
bool esPalindromo(stringConsumer str&){
	if (str.lenght() == 0) {
		exit(1);
	}
	int size = str.lenght();
	tPila A;
	tCola B;
	for (i = 0; i < str.size()%2; i++) {
		A.push( str.extratChar());
	}
	str.extractChar();
	for (i = 0; i < str.size(); i++) {
		B.enqueue(str.extractChar())
	}
	
	while (B.size() > 0) { //va sacando los elementos de las pilas hasta que una se quede vacia
		if (A.topValue() != B.frontValue()){
			return false
		} 
		A.pop();
		B.dequeue();
	}
	
}
