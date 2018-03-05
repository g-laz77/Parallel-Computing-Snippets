#include <stdio.h>
#include <stdlib.h>
#include <iostream>
using namespace std;
int main()
{
    // Assume 4x4 sparse matrix
    int m1 = 4, n1 = 4, m2 = 4, n2 = 4;
    int sparseMatrix1[m1][n1]; 
    int sparseMatrix2[m2][n2]; 
    //-----------------------------------------------------------------------Sparse matrix 1-------------------------------------------------------------------

    for (int i=0;i<m1;i++)
    {
        for(int j=0;j<n1;j++)
        {
            int k = rand()%2;
            if(!k)
                sparseMatrix1[i][j] = rand()%9;
            else    
                sparseMatrix1[i][j] = 0;
        }
    }
    cout<<"Matrix1:\n\n";
    for (int i=0;i<m1;i++)
    {
        for(int j=0;j<n1;j++)
            cout<<sparseMatrix1[i][j]<<" ";
        cout<<"\n";
    }
    printf("\n");
    
    int size1 = 0;
    for (int i = 0; i < m1; i++)
        for (int j = 0; j < n1; j++)
            if (sparseMatrix1[i][j] != 0)
                size1++;
 
    int compactMatrix1[3][size1];
 
    int k = 0;
    for (int i = 0; i < m1; i++){
        for (int j = 0; j < n1; j++){
            if (sparseMatrix1[i][j] != 0)
            {
                compactMatrix1[0][k] = i;
                compactMatrix1[1][k] = j;
                compactMatrix1[2][k] = sparseMatrix1[i][j];
                k++;
            }
        }
    }
    cout<<"Sparse Matrix 1:\n\n";
    for (int i=0; i<3; i++)
    {
        for (int j=0; j<size1; j++)
            printf("%d ", compactMatrix1[i][j]);
        printf("\n");
    }
    printf("\n");
    //-----------------------------------------------------------------------Sparse matrix 2-------------------------------------------------------------------
    
    for (int i=0;i<m2;i++)
    {
        for(int j=0;j<n2;j++)
        {
            int k = rand()%2;
            if(!k)
                sparseMatrix2[i][j] = rand()%9;
            else    
                sparseMatrix2[i][j] = 0;
        }
    }
    cout<<"Matrix2:\n\n";
    for (int i=0;i<m2;i++)
    {
        for(int j=0;j<n2;j++)
            cout<<sparseMatrix2[i][j]<<" ";
        cout<<"\n";
    }
    printf("\n");    
    int size2 = 0;
    for (int i = 0; i < m1; i++)
        for (int j = 0; j < n1; j++)
            if (sparseMatrix2[i][j] != 0)
                size2++;
 
    int compactMatrix2[3][size2];
 
    k = 0;
    for (int j = 0; j < n2; j++){
        for (int i = 0; i < m2; i++){
            if (sparseMatrix2[i][j] != 0)
            {
                compactMatrix2[0][k] = i;
                compactMatrix2[1][k] = j;
                compactMatrix2[2][k] = sparseMatrix2[i][j];
                k++;
            }
        }
    }
    cout<<"Sparse Matrix 2:\n\n";
    for (int i=0; i<3; i++)
    {
        for (int j=0; j<size2; j++)
            printf("%d ", compactMatrix2[i][j]);
        printf("\n");
    }
    printf("\n");
    
    //-----------------------------------------------------------------------product matrix-------------------------------------------------------------------
    int c[m1][n2];
    for (int i =0; i<m1; i++){
        for (int j=0;j<n2;j++)
            c[i][j] = 0;
    }

    
    for(int i =0; i<size1; i++){
        for(int j=0;j<size2;j++)
        {
            if (compactMatrix1[1][i] == compactMatrix2[0][j]){
                c[compactMatrix1[0][i]][compactMatrix2[1][j]] += compactMatrix1[2][i]*compactMatrix2[2][j];
            }                
        }
        
    }
    cout<<"Product:\n\n";
    for (int i =0; i<m1; i++){
        for (int j=0;j<n2;j++){
            cout<<c[i][j]<<" ";
        }
        cout<<"\n";
    }
    return 0;
}