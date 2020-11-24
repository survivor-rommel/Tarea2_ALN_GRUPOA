#include <bits/stdc++.h> 
using namespace std; 

// ---------------------- Matriz de vandermonde  ----
void GenararMatVandermonde(float V[20][20], int tam , float inicia , float rango){
    float x[tam];
    for (int l = 0; l < tam; l++) //rellenar en x[l]
    {
        x[l] = inicia;
		inicia = inicia + rango;
    }
	//crea la matriz
    for ( int i = 0; i < tam; i++)
        for (int j = 0; j < tam; j++)
            {
                V [i][j] = pow(x[i] , j);
			}
	// Se muestra la matriz de vandermonde
    /*for (int i = 0 ; i < tam ; ++i) 
    {
        for (int j = 0 ; j < tam ; ++j)
            cout << V [ i ] [ j ] << " " ;
                cout << "\n" ;
    }*/
}
// ---------------------- Genera una Matriz Hilbert ---- 
void GenearMatHilbert(float H[20][20] , int tam){ 
	 // Genera la matriz de Hilbert
    for (int i = 0; i < tam; i++) { 
        for (int j = 0; j < tam; j++) { 
            H[i][j] = (float)1.0/((i + 1) + (j + 1) - 1.0); 
        } 
    } 
	 // Se muestra la matriz de Hilbert
    /*for (int i = 0; i < tam; i++) { 
        for (int j = 0; j < tam; j++)  
            cout << H[i][j] << "   ";         
        cout << endl; 
    } */
} 

//-----------------------   Suma maxima de las columnas 
float Max_sumaCol(float M[20][20],int tam){
    float c_max = 0;
	float c_sum =0;
    for(int i=0 ; i<tam ; i++){
        c_sum =0;
        for(int j=0 ; j< tam ; j++){
            c_sum =abs(M[j][i])+ c_sum ;
        }
        c_max = max(c_max,c_sum);
    }
    return c_max; // devuelve la columna con la suma maxima
}
//-----------------------   Suma maxima de las filas 
float Max_sumaFila(float M[20][20],int tam){
    float f_max=0.0;
	float f_sum=0.0;
    for(int i=0 ; i<tam ; i++){
        f_sum=0;
        for(int j=0 ; j<tam ; j++){
            f_sum = abs(M[i][j]) + f_sum;
        }
        f_max = max(f_max,f_sum);
    }
    return f_max; // devuelve la fila con la suma maxima
}

//---------------------    Inversa de una matriz 
bool MatrizInv( float M[20][20], float inv[20][20] , int tam){
	bool vf= false;
	int cof[tam][tam],adj[tam][tam],cofaux[tam][tam],aux_inv[tam][tam];
	int i=0,j=0,det=0,det2=0,det3=0,det4=0,det5=0,aux_cof=1,d=0,k=0,e=0;
	for( i=0;i<tam;i++){
        for( j=0;j<tam;j++){
            for( d=0;d<tam;d++){
            for( e=0;e<tam;e++){
            for( k=0;k<tam;k++){
                    if((i+k)%2==0){
                        aux_cof = 1;
					}
                    else if((i+k)%2!=0){
                        aux_cof= -1;
                    }
                    if((d==k || d!=k) && (e==k || e==d)){
                        cofaux[i][j]= aux_cof*((M[i][k]*M[d][j])-(M[i][k]*M[e][j]));
                    }
            }
			}
			}
		}
    }
    for( i=0;i<tam;i++){
        for( j=0;j<tam;j++){
            cof[i][j]= cofaux[i][j];
        }
    }
    for( i=0;i<tam;i++){
        for(j=0;j<tam;j++){
                adj[i][j] = cof[j][i];
 
        }
    }
    //buscamos determinante
    for( i=0;i<tam;i++){
        for( j=0;j<tam;j++){
            for( k=0;k<tam;k++){
                for( e=0;e<tam;e++){
                    det=0;
                    det2=0;
                    for(d=0;d<tam;d++){
                        if((d!=k || d==k) && (e==k || e==d)&& i!=j){
                            if(i%2==0 & j%2==0 ){
                                det= det + ((M[i][d]*M[k][j])-(M[i][e]*M[d][j]));
                            }
                            else if(i%2!=0 && j%2!=0 ){
                                det2= det-((M[i][d]*M[k][j])-(M[i][d]*M[e][j]));
                            }
                        }
                        if(i==j){
                                det3= det3 +(M[i][j]*det);
                                det4= det4 +(M[i][j]*det2);
                        }
                    }
                }
            }
        }
    }
    det5 = det3 + det4;
    if(det5==0){
        return false;
    }
    else{
        for(i=0;i<tam;i++){
            for(j=0;j<tam;j++){
                aux_inv[i][j]= (1/det5)*adj[i][j];
                inv[i][j] = aux_inv[i][j];
            }
        }
		return true;
    }
}

//---------------------------   Condicionamiento Norma 1
float Norma1(float M[20][20],float MInv[20][20],int tam){
    float maxMat=0.0;
	float maxMatInv = 0.0;
	//El  Maximo de n Columnas de las matriz y matriz inversa
    maxMat=Max_sumaCol(M,tam);
    maxMatInv=Max_sumaCol(MInv,tam);
    return maxMat*maxMatInv;
}

float NormaFrobenius(float M[20][20],int tam){
    float sum=0;
    for(int i=0 ; i<tam ; i++){
        for(int j=0 ; j<tam ; j++){
            sum=pow(M[j][i],2)+sum;
        }
    }
    return sqrt(sum);
}

//---------------------------   Condicionamiento Norma 2
float Norma2(float M[20][20],float MInv[20][20],int tam){
    float maxMat=0.0;
	float maxMatInv = 0.0;
	
    maxMat = NormaFrobenius(M,tam);
    maxMatInv = NormaFrobenius(MInv,tam);
    return maxMat*maxMatInv;
}

//---------------------------   Condicionamiento Norma infinito
float NormaInf(float M[20][20],float MInv[20][20],int tam){
    float maxMat=0.0;
	float maxMatInv = 0.0;
	// El  Maximo de n Filas de las matriz y matriz inversa
    maxMat=Max_sumaFila(M,tam);
    maxMatInv=Max_sumaFila(MInv,tam);
    return maxMat*maxMatInv;
}

int main() { 
	int n = 0;
	float inicia ,rango = 0.0;
	bool M1 = false;
	bool M2 = false;
	float H[n][20] , Hinv[n][20];
	float V[n][20] , Vinv[n][20];
	
	cout<<endl;
	// ------- Matriz de vandermonde -----------------
		cout << " ------- MATRIZ DE VANDERMONDE --------";
		cout<<endl;
		cout<< "INGRESE EL TAMANO DE LA MATRIZ CUADRADA : ";
		cin>>n;
		cout<<endl;
		cout<<"Rellenar las " << n <<" filas con una rango de : ";
		cin>>rango;
		cout<<endl;
		cout<<"Iniciando Desde : ";
		cin>>inicia;
		cout<<endl;
		GenararMatVandermonde(V,n,inicia,rango); 
		//calculo la matriz inversa para el condicionamiento
		MatrizInv(V,Vinv,n);
		cout << "    Norma 1     " ;
		cout<<Norma1(V,Vinv,n);
		cout<<endl;
		cout << "    Norma 2     " ;
		cout<<Norma2(V,Vinv,n);
		cout<<endl;
		cout << " Norma Infinita " ;
		cout<<NormaInf(V,Vinv,n);		
		cout<<endl<<endl;	
		
	// ------- Genera una Matriz Hilbert -------------
		cout << " ------- MATRIZ DE HILBERT --------";
		cout<<endl;
		cout<< "INGRESE EL TAMANO DE LA MATRIZ CUADRADA : ";
		cin>>n;
		GenearMatHilbert(H,n);
		//calculo la matriz inversa para el condicionamiento
		MatrizInv(H,Hinv,n);
        cout <<    " Norma 1     " ;
		cout<<Norma1(H,Hinv,n);
		cout << "    Norma 2     " ;
		cout<<Norma2(H,Hinv,n);
		cout << " Norma Infinita " ;
		cout<<NormaInf(H,Hinv,n);
		
}