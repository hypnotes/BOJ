#include <stdio.h>

int cycle(int init, int xy, int count){

   
    if(init == xy && count > 0){
        printf("%d", count);
        return 0;
    }
    count++;

    int x = xy%10;  //24중 '4' (두번째 숫자)
    int y = (xy/10+xy%10)%10; //2+4 = 08 중 '8' (두번째 숫자)
    int new = x*10+y;
    cycle(init, new, count);
}

int main(void){
    int n;
    scanf("%d", &n);

    cycle(n, n, 0);

    return 0;
}