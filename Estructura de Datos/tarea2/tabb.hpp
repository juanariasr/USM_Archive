using namespace std;	

typedef float tipoElem;

struct monomio{
			float exp;
			float coef;
		};
		
typedef struct tNodoArbolBin{
	monomio info;
	tNodoArbolBin* izq;
	tNodoArbolBin* der;
}tNodo;

class tABB {
	private:
		
		tNodo *raiz;
		
		int nElems;
		
		
	
	public:
		tABB();
		
		//~tABB(); //lo mismo que clear?
		
		int find(float exponente);
		
		int size();
		
		void inOrden(tipoElem n);
		
		void preOrden();
		
		void postOrden();
		
		void insert(tNodoArbolBin *&arbol, monomio m, tipoElem exp);
		
		void remove();
		
		void clear();
};

tABB::tABB (){ //constructor
			raiz = NULL;
			nElems = 0;
		}
		
int tABB::size(){ //tamaño del arbol?
			return nElems;
		}	
	
	
void clearHelp(tNodo* nodo){
		if (nodo == NULL) return; //arbol vacio se detiene
		clearHelp(nodo->izq); //visita subarbol izquierdo recursivamente
		clearHelp(nodo->der); //visita arbol derecho recursivamente
		delete nodo; //despues de borrar subarboles, se borra a si mismo
	}
		
void tABB::clear() {
			clearHelp(raiz); //funcion auxiliar para eliminar nodos, funcion recursiva que recorre en postorden
			raiz = NULL;
			nElems = 0;
		}

int findHelp(tNodoArbolBin* nodo, tipoElem item) {
	if (nodo == NULL) return 0; //item no esta en el arbol
	if (nodo->info.exp == item) return 1; //item encontrado
	if (item <  nodo -> info.exp)
		return findHelp(nodo->izq,item);
	else
		return findHelp(nodo->der, item);
}
		
int tABB::find(tipoElem item) { //busca un item en un ABB T, retorna 0 en caso de no encontrarlo
	return findHelp(raiz, item);
}

void inOrdenHelp (tNodoArbolBin* nodo, tipoElem n) {
	if (nodo == NULL) return; //arbol vacio se detiene
	inOrdenHelp (nodo->izq, n); //visita hijo izq en in orden
	//procesar (nodo->info); //procesa nodo actual
	inOrdenHelp (nodo->der, n); //visita hijo derecho en in orden
}


void tABB::inOrden(tipoElem n) { //recorrido inorden de un ABB T
	inOrdenHelp(raiz, n); 
}

tNodoArbolBin *crearNodo(monomio n) { //funcion que crea un nuevo nodo
	tNodoArbolBin *nuevo_nodo = new tNodoArbolBin();
	
	nuevo_nodo -> info = n;
	nuevo_nodo -> der = NULL;
	nuevo_nodo->izq = NULL;
	
	return nuevo_nodo;
}

void tABB::insert(tNodoArbolBin *&arbol, monomio n, tipoElem exp){ //inserta un elemento item en el ABB
	if (raiz == NULL) { //si el arbol esta vacio
		tNodoArbolBin *nuevo_nodo = crearNodo(n);
		arbol = nuevo_nodo;
	}
	else{ //si el arbol tiene uno o mas nodos
		int valorRaiz = arbol->info.exp; //info
		if (exp < valorRaiz){
			insert(arbol->izq,n, exp); //si el elemento es menor que la raiz, se inserta a la izq
		}
		else {
			insert(arbol->der,n, exp); //si el elemento es mayor que la raiz, se inserta a la izq
		}
		
	}
	nElems++;
	
}



