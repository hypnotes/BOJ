#include <stdio.h>


int main(void){
    int a;
    scanf("%d", &a);
    int ans = 1;
    if(a > 1){
        for(int i = 2; i<=a; i++) ans*=i;
    }
    printf("%d", ans);
}