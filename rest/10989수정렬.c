#include <stdio.h>

//평소 sort가 아니라 배열에 저장하고 카운트 방식으로 해야 8MB를 안넘음
int ARR[10001] ={0,};

int main(void){
    int num;
    scanf("%d", &num);
    int i, a;
    for(i =0; i<num; i++){
        scanf("%d", &a);
        ARR[a]++;
    }
    for(i = 0; i<10001; i++){
        if(ARR[i]!=0){
            for(int j = 0; j<ARR[i]; j++) printf("%d\n", i);
        }
    }
    return 0;
}