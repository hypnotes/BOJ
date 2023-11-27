#include <stdio.h>

int selfNum(int num){
    int ans = num;
    while(num>0){
        ans+=num%10;
        num/=10;
    }
    return ans;
}

int main(void){
    int array[10001];
    for(int i=1; i<=10001; i++){
        int check = selfNum(i);
        if(check < 10001) array[check] =1;
    }
    for(int i=1; i<10001; i++){
        if(array[i]!=1) printf("%d\n", i);
    }
    return 0;
}