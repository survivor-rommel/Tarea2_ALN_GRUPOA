#include <iostream>

//factor
void getCfactor(double M[100][100], double t[][100], int p, int q, int n) {
   int i = 0, j = 0;
   for (int r= 0; r< n; r++) {
      for (int c = 0; c< n; c++){
         if (r != p && c != q) { 
            t[i][j++] = M[r][c];
            if (j == n - 1) {
               j = 0; i++;
   }}}}}

//determinante
double DET(double M[100][100], int n){
   double D = 0;
   if (n == 1)
      return M[0][0];
   double t[n][100];
   double s = 1; 
   for (int f = 0; f < n; f++) {
      getCfactor(M, t, 0, f, n); D += s * M[0][f] * DET(t, n - 1);
      s = -s;
   }
   return D;
}

void ADJ(double M[100][100],double adj[100][100],int n)
{
   if (n == 1) {
      adj[0][0] = 1; return;
   }
   double s = 1;
   double t[n][100];
   for (int i=0; i<n; i++) {
      for (int j=0; j<n; j++) {
         getCfactor(M, t, i, j, n);
         s = ((i+j)%2==0)? 1: -1; 
         adj[j][i] = (s)*(DET(t, n-1));
   }}}

//inversa
bool INV(double M[100][100], double inv[100][100],int n) {
   double det = DET(M, n);
   if (det == 0) {
      std::cout << "\nNo se puede hallar inversa\n";
      return false;
   }
   double adj[n][100]; 
   ADJ(M, adj,n);
   for (int i=0; i<n; i++) for (int j=0; j<n; j++) inv[i][j] = adj[i][j]/double(det);
   return true;
}
