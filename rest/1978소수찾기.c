#include <stdio.h>

int isSosu(int num){

    if(num == 1) return 0;
    for(int i = 2; i<num/2+1; i++){
        if(num%i == 0) return 0;
    }
    return 1;

}
int main(void){

    int a;
    scanf("%d", &a);
    int ans = 0;
    for(int i = 0; i<a; i++){
        int b;
        scanf("%d", &b);
        if(isSosu(b)) ans++;
    }
    printf("%d", ans);
}