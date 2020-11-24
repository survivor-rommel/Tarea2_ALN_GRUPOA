#include <iostream>
#include "inverse_Matrix.h"
#include <math.h> //para usar raiz cuadrada y potencia

//imprimir matriz
template<class T> void print(T A[][100],int n) 
{
   for (int i=0; i<n; i++) { 
      for (int j=0; j<n; j++) 
         std::cout << A[i][j] << " "; 
      std::cout << std::endl;
   }
}

//absoluto de un número
double Abs(double x)
{
    if(x<0)
        x=x*-1;
    return x;
}

//creación de matriz simple
void Matrix(double A[100][100], int n) {  
    for(int i=0;i<n;i++){
            std::cout<<"Fila "<<i+1<<":"<<std::endl;
            for(int j=0;j<n;j++){
                std::cout<<"["<<i<<"]"<<"["<<j<<"]  : ";
                std::cin>>A[i][j];
            }
    }
} 

//creación de matriz de Hilbert
void HilbertMatrix(double H[100][100], int n) {  
    for (int i = 0; i < n; i++) { 
        for (int j = 0; j < n; j++) { 
            H[i][j] = (double)1.0/((i + 1) + (j + 1) - 1.0); 
        } 
    } 
} 

//creación de matriz de Vandermonde 
void VanderMatrix(double V[100][100], int n) {
    double interpolacion=0.5,x=1;
    std::cout<<"Rango de salto: ";
    std::cin>>interpolacion;
    std::cout<<"Comienza en: ";
    std::cin>>x;
    for(int i=0;i<n;i++){
        V[i][0]=1;
        for(int j=1;j<n;j++)
            V[i][j]=V[i][j-1]*x;
        x+=interpolacion;
    }
}

//NormaFrobenius
double NormaFrobenius(double A[100][100],int n){
    double sum=0;
    for(int i=0 ; i<n ; i++){
        for(int j=0 ; j<n ; j++){
            sum=pow(A[j][i],2)+sum;
        }
    }
    return sqrt(sum);
}

//Condición con norma de Frobenius / norma 2
double Cond2(double A[100][100],double B[100][100],int n){
    double max1=0, max2;
    max1=NormaFrobenius(A,n);
    max2=NormaFrobenius(B,n);
    return max1*max2;
}

//Máxima suma absoluta de entre las columnas de una matriz
double maxSumXCol(double A[100][100],int n){
    double max=0,sum;
    for(int i=0 ; i<n ; i++){
        sum=0;
        for(int j=0 ; j<n ; j++){
            sum=Abs(A[j][i])+sum;
        }
        if(sum>max)
            max=sum;
    }
    return max;
}

//Condición con norma 1
double Cond1(double A[100][100],double B[100][100],int n){
    double max1=0, max2;
    max1=maxSumXCol(A,n);
    max2=maxSumXCol(B,n);
    return max1*max2;
}

//Máxima suma absoluta de entre las columnas de una matriz
double maxSumXFila(double A[100][100],int n){
    double max=0,sum;
    for(int i=0 ; i<n ; i++){
        sum=0;
        for(int j=0 ; j<n ; j++){
            sum=Abs(A[i][j])+sum;
        }
        if(sum>max)
            max=sum;
    }
    return max;
}

//Condición con norma infinito
double CondInf(double A[100][100],double B[100][100],int n){
    double max1=0, max2;
    max1=maxSumXFila(A,n);
    max2=maxSumXFila(B,n);
    return max1*max2;
}

int main()
{
    std::cout<<"========================================\n";
    std::cout<<"Condicionamiento de una matriz\n";
    std::cout<<"========================================\n";
    int n,op;
    std::cout<<"Ingrese el tamanio de la matriz: ";
    std::cin>>n;
    double A[n][100],B[n][100];
    while(true){
        std::cout<<"\nCrear matriz tipo:\n1. Simple\n2. Hilbert\n3. Vandermonde\nOpcion: ";
        std::cin>>op;
        if(op==1){ //matriz simple 
            Matrix(A,n);
            break;
        }
        else if(op==2){ //matriz de Hilbert
            HilbertMatrix(A,n);
            break;
        }
        else if(op==3){ //matriz de Vander
            VanderMatrix(A,n);
            break;
        }
        else
            std::cout<<"\nOpcion invalida\n";
    }     
    std::cout<<"\nMatriz creada\n";
    std::cout<<"========================================\n";
    std::cout<<"Resultado:\n";
    std::cout<<"========================================\n";
    if(INV(A,B,n)==true){ //si tiene inversa la matriz se procede a calcular el condicionamiento
        std::cout<<"Inversa hallada\n\nNorma 1:\n";
        std::cout<<Cond1(A,B,n);
        std::cout<<"\nNorma 2 o Frobenious:\n";
        std::cout<<Cond2(A,B,n);
        std::cout<<"\nNorma infinito:\n";
        std::cout<<CondInf(A,B,n);
    }    
    std::cout<<"\n\nEnter para salir";
    std::cin.get();
    std::cin.get();
    return 0;
}