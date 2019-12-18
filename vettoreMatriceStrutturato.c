#include <stdio.h>
#include <stdlib.h>
#include <time.h>

struct Cella {
    int i;
    int j;
    int val;
};

void printVector(int* vet, int n){
    for (int i = 0; i < n; i++){
        printf("%d ",vet[i]);
    }
    printf("\n");
}

int main(){
    int n = 3;
    int A[n][n],v[n];
    srand(time(NULL));
    for (int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            A[i][j] = rand() % 5;
            printf("%d ",A[i][j]);
        }
        printf("\n");
    }
    printf("\n\n");
    for (int i = 0; i < n; i++) {
        v[i] = rand() % 5;
    }

    struct Cella mat[n];
    int k = 0;
    struct Cella cella;
    int res[n];
    for (int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            if(A[i][j]!=0){
                cella.i = i;
                cella.j = j;
                cella.val = A[i][j];
                mat[k] = cella;
                k++;
            }
        }
    }
    printf("\n");

    for(int i = 0; i < k; i++) {
        printf("%d %d %d\n",mat[i].i,mat[i].j,mat[i].val);
    }
    for(int i = 0; i < n; i++) {
        res[i] = 0;
    }
    printf("\n\n");
    printVector(v,n);
    printf("\n\n");
    for(int l = 0; l < k; l++) {
        res[mat[l].i] += (mat[l].val * v[mat[l].j]);
    }
    printVector(res,n);
}