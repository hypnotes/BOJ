
#include <stdio.h>

int main(void){
    int a;
    scanf("%d", &a);
    int i;
    int cur = 2;
    if(a==1) printf("%d", 1);
    else if(a<8) printf("%d", 2);
    else{
        for(i = 1; cur <= a; ){
            i++;
            cur = 6 * (i-1) + cur;
        }

        printf("%d ", i);
    }
}


/*
#include <stdio.h>
int arr[100000000];

int func(int num){
    int i;
    int cur = 2;//arr[1] = 2;
    if(num==1) printf("%d", 1);
    else if(num<8) printf("%d", 2);
    else{
        for(i = 1; cur <= num; ){
            i++;
            cur = 6 * (i-1) + cur;
        }
        printf("%d ", i);
    }
    printf("\n");
    return 1;
}
int main(void){
    int a;
    scanf("%d", &a);
    func(a);
    while(a!=0){
        scanf("%d", &a);
        func(a);
    }
    
}
*/