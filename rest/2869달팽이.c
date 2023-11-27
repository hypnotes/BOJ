#include <stdio.h>
#include <math.h>

int main(void){

    double a, b, v, d;
    scanf("%d%d%d", &a, &b, &v);
    
    printf("%0.0lf", ceil((v-a)/(a-b))+1);

}