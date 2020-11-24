#include <iostream>
#include <cmath>
using namespace std;

//factor
void getCfactor(double M[100][100], double t[][100], int p, int q, int n) {
   int i = 0, j = 0;
    for (int r= 0; r< n; r++) {
        for (int c = 0; c< n; c++){
            if (r != p && c != q) { 
                t[i][j++] = M[r][c];
                if (j == n-1) {j=0;i++;}
            }
        }
    }
}

//determinante
double DET(double M[100][100], int n){
    double D = 0;
    if (n == 1)
        return M[0][0];
    double t[n][100];
    double s = 1; 
    for (int i=0; i<n; i++){
        getCfactor(M, t, 0, i, n);
        D += s*M[0][i]*DET(t, n - 1);
        s = -s;
    }
    return D;
}

void ADJ(double M[100][100],double adj[100][100],int n)
{
    if (n == 1) {adj[0][0] = 1; return;}
    double s = 1;
    double t[n][100];
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            getCfactor(M, t, i, j, n);
            s = ((i+j)%2==0)? 1: -1; 
            adj[j][i] = (s)*(DET(t, n-1));
        }
    }
}

//inversa
bool INV(double M[100][100], double inv[100][100],int n) {
    cout<<"Entrando determinante"<<endl;
    double det = DET(M, n);
    if (det == 0) {
        cout << "\nNo se puede hallar inversa\n";
        return false;
    }
    double adj[n][100]; 
    ADJ(M, adj,n);
    for (int i=0; i<n; i++) for (int j=0; j<n; j++) inv[i][j] = adj[i][j]/double(det);
    return true;
}


//imprimir matriz
template<class T> void print(T A[][100],int n) 
{
    for (int i=0; i<n; i++) { 
        for (int j=0; j<n; j++) 
            cout << A[i][j] << " "; 
    cout << endl;
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
            for(int j=0;j<n;j++){
                cout<<"M"<<i+1<<j+1<<": ";
                cin>>A[i][j];
            }
    }
} 

//creación de matriz de Hilbert
void HilbertMatrix(double H[100][100], int n) {  
    for (int i=0; i<n; i++) { 
        for (int j=0; j<n; j++) {
            H[i][j] = (double)1.0/((i + 1) + (j + 1) - 1.0); 
        } 
    } 
} 

//creación de matriz de Vandermonde 
void VanderMatrix(double V[100][100], int n) {
    double interpolacion=0.5,x=1;
    cout<<"Rango de salto: ";
    cin>>interpolacion;
    cout<<"Comienza en: ";
    cin>>x;
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
    cout<<"Condicionamiento de una matriz\n";
    int n,op;
    cout<<"Tamanio Matriz nxn: ";
    cin>>n;
    double A[n][100],B[n][100];
    while(true){
        cout<<"\nCrear matriz tipo:\n1. Simple\n2. Hilbert\n3. Vandermonde\nOpcion: ";
        cin>>op;
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
            cout<<"\nOpcion invalida\n";
    } 
    cout<<"\nResultado:\n";
    if(INV(A,B,n)==true){ //si tiene inversa la matriz se procede a calcular el condicionamiento
        cout<<"Norma 1:\t\t";
        cout<<Cond1(A,B,n);
        cout<<"\nNorma 2 o Frobenious:\t";
        cout<<Cond2(A,B,n);
        cout<<"\nNorma infinito:\t\t";
        cout<<CondInf(A,B,n);
    }


    return 0;
}