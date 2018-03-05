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
 
    int csrMatrix1[2][size1];
    int csrClRow1[m1+1];
    csrClRow1[0] = 0;
    int k = 0;
    int count;
    for (int i = 0; i < m1; i++){
        count = 0;
        for (int j = 0; j < n1; j++){
            if (sparseMatrix1[i][j] != 0)
            {
                count++;
                csrMatrix1[0][k] = j;
                csrMatrix1[1][k] = sparseMatrix1[i][j];
                k++;
            }
        }
        csrClRow1[i+1] = csrClRow1[i] + count;
    }
    cout<<"CSR Matrix 1:\n\n";    
    for(int i =0;i<size1;i++)
        cout<<csrMatrix1[0][i]<<" ";
    cout<<"\n";
    for(int i =0;i<size1;i++)
        cout<<csrMatrix1[1][i]<<" ";
    cout<<"\n";
    for(int i =0;i<m1+1;i++)
        cout<<csrClRow1[i]<<" ";
    cout<<"\n\n";
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
    for (int i = 0; i < m2; i++)
        for (int j = 0; j < n2; j++)
            if (sparseMatrix2[i][j] != 0)
                size2++;
 
    int csrMatrix2[2][size2];
    int csrClRow2[m1+1];
    csrClRow2[0] = 0;
    k = 0;
    for (int i = 0; i < m2; i++){
    
        count = 0;
        for (int j = 0; j < n2; j++){
            if (sparseMatrix2[i][j] != 0)
            {
                count++;
                csrMatrix2[0][k] = j;
                csrMatrix2[1][k] = sparseMatrix2[i][j];
                k++;
            }
        }
        csrClRow2[i+1] = csrClRow2[i] + count;
    }
    cout<<"CSR Matrix 2:\n\n";
    for(int i =0;i<size2;i++)
        cout<<csrMatrix2[0][i]<<" ";
    cout<<"\n";
    for(int i =0;i<size2;i++)
        cout<<csrMatrix2[1][i]<<" ";
    cout<<"\n";
    for(int i =0;i<m1+1;i++)
        cout<<csrClRow2[i]<<" ";
    cout<<"\n\n";

//-----------------------------------------------------------------------Product matrix-------------------------------------------------------------------

    int c[m1][n2];
    for (int i =0; i<m1; i++){
        for (int j=0;j<n2;j++)
            c[i][j] = 0;
    }
    for(int i=1;i<m1+1;i++){
        for(int j = 1;j<m2+1;j++)
        {
            for(int k = csrClRow1[i-1];k<csrClRow1[i];k++){
                for(int l = csrClRow2[j-1];l<csrClRow2[j];l++)
                {
                    if(csrMatrix1[0][k] == j-1)
                        c[i-1][csrMatrix2[0][l]]+= csrMatrix1[1][k] * csrMatrix2[1][l];
                }
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

