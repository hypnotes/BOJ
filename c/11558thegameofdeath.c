#include <stdio.h>
//FAIL
int main(void){

    int t;

    scanf("%d", &t);

    for(int i=0; i<t; i++){
        int n;
        scanf("%d", &n);
        int li[n];
        for(int j = 0; j<n ; j++ ) scanf("%d", &li[j]);
        
        int k = 1;
        int pointed = li[0];
        for(int j = 0; j<sizeof(li)/sizeof(int); j++) printf("%d ", li[j]);
        printf("\n");
        while( k!=n && pointed!=n){
            pointed = li[pointed-1];
            k++;
        }

        k == n ?  printf("0") : printf("%d\n", k);

    }

}