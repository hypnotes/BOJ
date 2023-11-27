#include <stdio.h>
#include <time.h>

//에라토스테네스의 체

int main(void){
    int m, n;
    scanf("%d%d", &m, &n);
    clock_t t;
    t=clock();
    for(int i = m; i<=n; i++){
        int j = 2;
        for(int j=2; j<i/2+1; j++){
            if(i%j==0) {
                break;}
        }
        if(j == i/2+1) printf("%d\n", i);
    }
    t = clock() - t;
    t = clock() - t;
    double time_taken = ((double)t)/CLOCKS_PER_SEC; // in seconds
  
    printf("fun() took %f seconds to execute \n", time_taken);
    return 0;
}