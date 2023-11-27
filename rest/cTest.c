#include <stdio.h>


int main(void){
    int m, n;
    
    scanf("%d%d", &m, &n);
    
    for(int i = m; i<= n; i++){
        printf("%d ", i );
    }
    
    return 0;
}