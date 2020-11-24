#include <iostream>
#include <cmath>

using namespace std;

void imprimir(long double **M, int n){
	for(int i = 0; i<n; i++){
		for(int j=0;j<n;j++){
			cout<<M[i][j]<<" ";
		}	
		cout<<endl;
	}
}

long double **identidad(int n){
	
	//Crear la matriz
	long double **A;
	A = new long double *[n];
	for(int a=0;a<n;a++){
		A[a] = new long double[n];
	}
	
	//Llenar la matriz
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			if(i==j)
				A[i][j]=1;
			else
				A[i][j]=0;
		}
	}
	
	return A;
}

long double** vandermonde(long double vec[], int n){
	
	//Crear la matriz
	long double **A;
	A = new long double *[n];
	for(int a=0;a<n;a++){
		A[a] = new long double[n];
	}
	
	int cont=n-1;
	//Llenar la matriz
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			A[i][j]=pow(vec[i],cont);
			cont--;
		}
		cont=n-1;
	}
	
	cout<<"Su matriz es: "<<endl;
	//Mostrar la matriz
	for(int b=0; b<n;b++){
		for(int q=0;q<n;q++){
			cout<<A[b][q]<<" ";
		}
		cout<<endl;
	}
	
	return A;
}

long double** hilbert(int n){
	
	//Crear la matriz
	long double **A;
	A = new long double *[n];
	for(int a=0;a<n;a++){
		A[a] = new long double[n];
	}
	
	//Llenar la matriz
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			long double aux= i+j;
			A[i][j]=1/(aux+1);
		}
	}
	
	cout<<"Su matriz es: "<<endl;
	//Mostrar la matriz
	for(int b=0; b<n;b++){
		for(int q=0;q<n;q++){
			cout<<A[b][q]<<" ";
		}
		cout<<endl;
	}
	return A;
}

long double** matriz_cuadrada(int n){
	//Crear la matriz
	long double **A;
	A = new long double *[n];
	for(int a=0;a<n;a++){
		A[a] = new long double[n];
	}
	
	//Llenar la matriz
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			cout<<"Ingrese el valor ["<<i+1<<"]["<<j+1<<"]: "; cin>>A[i][j];
		}
	}
	
	cout<<"Su matriz es: "<<endl;
	//Mostrar la matriz
	for(int b=0; b<n;b++){
		for(int q=0;q<n;q++){
			cout<<A[b][q]<<" ";
		}
		cout<<endl;
	}
	return A;
}

long double **copia(long double ** A, int n){
	long double **copia;
	copia = new long double *[n];
	
	for(int a=0;a<n;a++){
		copia[a] = new long double[n];
	}
	
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			copia[i][j]=A[i][j];
		}
	}
	return copia;
}

long double ** inversa(long double **M, int n){
	
	short int i,j,k;
	long double **I, aux, pivote, **A;
	
	A = new long double *[n];
	I = new long double *[n];
	for(int a=0;a<n;a++){
		A[a] = new long double[n];
		I[a] = new long double[n];
	}
	
	for(i=0; i<n; i++){
		for(j=0; j<n; j++){
			A[i][j] = M[i][j];
		}
	}
	
	for(i=0; i<n; i++){
		for(j=0; j<n;j++){
			I[i][j]=0;
			if(i==j){
				I[i][j]=1;
			}
		}
	}
	
	//Reduccion por renglones
	for(i=0; i<n; i++){
		pivote=A[i][i];
		
		//Convertir pivote a 1
		for(k=0; k<n; k++){
			A[i][k] = A[i][k]/pivote;
			I[i][k] = I[i][k]/pivote;
		}
		
		for(j=0; j<n; j++){
			if(i!=j){    //No estamos en la diagonal
				aux=A[j][i];
				for(k=0; k<n; k++){
					A[j][k] = A[j][k]-aux*A[i][k];
					I[j][k] = I[j][k]-aux*I[i][k];
				}
			}   
		}
		
		
	}

	
	return I;
}

long double sumatoria(long double **A, int indice, char modo, int n){
	long double suma= 0;
	if(modo=='j'){
		for(int i=0;i<n; i++){
			
			suma+=abs(A[i][indice]);
		}
		return suma;
	}
	else if(modo='i'){
		for(int j=0; j<n; j++){
			suma+=abs(A[indice][j]);
		}
		return suma;
	}
}

long double **transpuesta(long double **A, int n){
	
	long double **T;
	T = new long double *[n];
	for(int a=0;a<n;a++){
		T[a] = new long double[n];
	}
	
	for(int i=0; i<n; i++){
		for(int j=0; j<n; j++){
			T[i][j]=A[j][i];
		}
	}	
	return T;
	
}

long double **multiplicacionMatricial(long double **A, long double **B, int n){
	
	long double subtotal;
	long double **Resultado = copia(A,n);
	for(int i=0; i<n; i++){
		for(int j=0; j<n; j++){
			subtotal = 0;
			for(int q=0;q<n;q++){
				subtotal += A[i][q]*B[q][j];
			}
			Resultado[i][j] = subtotal;
			
		}
	}
	return Resultado;
}

long double *multiplicacionMatrizVector(long double **A, long double *B, int n){
	long double *Resultado = new long double[n];
	long double subtotal;
	for(int i=0; i<n; i++){
		subtotal = 0;
		for(int j=0; j<n; j++){
			subtotal += A[i][j]*B[j];
		}
		Resultado[i]=subtotal;
	}
	return Resultado;
}

long double metodo_potencias(long double **A, int n){
	long double* vec = new long double[n];
	vec[0] = 1;
	for(int i=1; i<n; i++){
		vec[i] = 0;
	}
	long double actual, anterior;
	long double Akv = vec[0];
	vec = multiplicacionMatrizVector(A,vec, n);
	long double Ak1v = vec[0];
	actual = Ak1v/Akv;
	
	for(int i=0; i<1000; i++){
		Akv = Ak1v;
		vec = multiplicacionMatrizVector(A, vec, n);
		Ak1v = vec[0];
		anterior = actual;
		actual = Ak1v / Akv;
		if(abs(anterior-actual)<1e-50){
			break;
		}
	}
	
	return actual;
	
}

long double norma_1(long double **A, int n){
	long double lista[n];
	long double elemento;
	for(int j=0; j<n; j++){
		elemento = sumatoria(A, j, 'j', n);
		lista[j] = elemento;
	}
	
	long double max = lista[0];
	
	//Buscar el maximo del vector
	for(int i=0;i<n;i++){
		if(lista[i]>max){
			max=lista[i];
		}
	}
	
	return max;
}

long double norma_2(long double **A, int n){
	long double **At = transpuesta(A,n);
	long double **MatrizResultado = multiplicacionMatricial(At, A, n);
	long double maximoEigenValue = metodo_potencias(MatrizResultado, n);
	return sqrt(maximoEigenValue);
}

long double norma_infinito(long double **A, int n){
	
	long double lista[n];
	long double elem;
	
	for(int i=0; i<n; i++){
		elem = sumatoria(A, i, 'i', n);
		lista[i] = elem;
	}
	
	long double max = lista[0];
	
	//Buscar el maximo del vector
	for(int i=0;i<n;i++){
		if(lista[i]>max){
			max=lista[i];
		}
	}
	
	return max;
}

int main(){
	
	cout<<"TRABAJO ALGEBRA LINEAL! HECHO POR: RODRIGO JESUS SANTISTEBAN PACHARI"<<endl;
	cout<<"Implementado en C++\nFunciona para\n-Matrices de Hilbert\n-Matrices Vandermonden\n-Matrices Cuadradas Simples"<<endl;
	cout<<"Trabaja con\n-Norma 1\n-Norma 2\n-Norma infinito"<<endl<<endl;
	
	int opc=-1;
	int opc2 =-1; 
	int n;
	long double resultado;
	long double **A;
	
	//Seleccion de matriz del usuario
	do{
		cout<<"\n1.Matriz de Hilbert\n2.Matriz Vandermonden\n3.Matriz Cuadrada\n";
		cin>>opc;
		
		if(opc==1){
			cout<<"Ingrese el tamanio de la matriz: "; cin>>n;
			A = hilbert(n);
		}
		
		else if(opc==2){
			cout<<"Ingrese el tamanio de la matriz "; cin>>n;
			cout<<"Ingrese su vector "<<endl;
			long double vec[n];
			for(int i=0; i<n; i++){
				cout<<"Posicion:["<<i+1<<"]: ";cin>>vec[i];
			}
			A = vandermonde(vec, n);
			
		}
		
		else if(opc==3){
			cout<<"Ingrese el tamanio de la matriz "; cin>>n;
			A = matriz_cuadrada(n);
		}
		
		else{
			cout<<"Opcion incorrecta"<<endl;
		}
		
	}while(opc>3 || opc<1);
	
	
	
	do{
		
		cout<<"\n1.Usar norma 1\n2.Usar norma 2\n3.Usar norma infinito\n";
		cin>>opc2;
		
		if(opc2==1){
			resultado = norma_1(A,n) * norma_1(inversa(A,n),n);
			cout<<endl<<"El resultado es: "<<resultado;
		}
		
		else if(opc2==2){
			resultado = norma_2(A,n) * norma_2(inversa(A,n),n);
			cout<<endl<<"El resultado es: "<<resultado;
		}
		
		else if(opc2==3){
			resultado = norma_infinito(A,n) * norma_infinito(inversa(A,n),n);
			cout<<endl<<"El resultado es: "<<resultado;
		}
		
		else{
			cout<<"Opcion incorrecta"<<endl;
		}
		
	}while(opc2>3 || opc2<1);
	return 0;
}
