#include <stdio.h>

int ppl(int k, int n, int ans){
    if(k==0) return n;
    for(int i = 1; i<=n; i++) ans += ppl(k-1, i, 0);
    return ans;
}

int main(void){
    int t;
    scanf("%d", &t);
    for (int i=0; i<t; i++){
        int k , n;
        scanf("%d", &k);
        scanf("%d", &n);
        printf("%d\n", ppl(k,n, 0));
    }

    return 0;
}