// #include <stdio.h>

// //RECURSION
// long long int fib(long long int f1, long long int f2, int n, int a){
//     if(n==a)    return f1;
//     fib(f2, f1+f2, n+1, a);
// }

// int main(void){
//     int a;
//     scanf("%d", &a);
//     printf("%lld", fib(0, 1, 0, a));
    
// }

#include <stdio.h>
#include <stdlib.h>

//for loop..pointers 없어도 same
int main(void){
    
    int i, a;
    scanf("%d", &a);

    long long int *f1 = (long long int*)malloc(8);
    long long int *f2 = (long long int*)malloc(8);
    long long int *temp = (long long int*)malloc(8);

    *f1 = 0;
    *f2 = 1;

    for(i =0; i<a; i++){
        printf("try: %d, %lld, %lld\n", i, *f1, *f2);
        *temp = *f1;
        *f1 = *f2;
        *f2 = *f1 + *(temp);
    }
    free(f2);
    free(temp);
    printf("%lld", *f1);
    free(f1);
    
}