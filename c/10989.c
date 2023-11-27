#include <stdlib.h>
#include <stdio.h>
//11개월전의 본인 코드와 https://yjyoon-dev.github.io/boj/2021/06/24/boj-10989/ 참고
int DATA[10001]= {0,};   //10001개 자리 다 0으로 initialize

int main(void){
    int n, i, a;
    scanf("%d", &n);

    for(i=0; i<n; i++){
        scanf("%d", &a);
        DATA[a]++;              //값만 받으면 해당 값 카운트 시작 (몇 번 나왔는지)
    }

    for(i=0; i<10001; i++){
        if(DATA[i]){
            for(int j = 0; j<DATA[i]; j++) 
                printf("%d\n", i);
        }
    }

}