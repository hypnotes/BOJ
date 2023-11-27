#include <stdio.h>

int main(void){
    
    int a;
    scanf("%d", &a);

    if(a>1){
        int arr[a+1];
        arr[0]=0;
        arr[1]=1;
        for(int i = 2; i<=a; i++) arr[i]=arr[i-1]+arr[i-2];
        printf("%d\n", arr[a]);
    }
    else printf("%d\n", a);

}