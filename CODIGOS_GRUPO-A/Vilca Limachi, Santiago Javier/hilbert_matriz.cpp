
// C++ program for Hilbert Matrix 
#include <bits/stdc++.h> 
using namespace std; 
  
// Function that generates a Hilbert matrix 
void printMatrix(int n) 
{ 
    float H[n][n]; 
  
    for (int i = 0; i < n; i++) { 
        for (int j = 0; j < n; j++) { 
  
            // using the formula to generate 
            // hilbert matrix 
            H[i][j] = (float)1.0 /  
                     ((i + 1) + (j + 1) - 1.0); 
        } 
    } 
  
    for (int i = 0; i < n; i++) { 
        for (int j = 0; j < n; j++)  
            cout << H[i][j] << " ";         
        cout << endl; 
    } 
} 
  
// driver function 
int main() 
{ 
    int n = 3; 
    printMatrix(n); 
    return 0; 
} 