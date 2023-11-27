#include <stdio.h>


int route(int x, int y){

    int dist = y-x;
    int count = 1;
    //int ans = 0;
    if(dist <= 3) return dist;
    else if(dist == 4) return 3;
    while(dist>count){
        dist -= count*2;
        //ans += 2;
        if(dist <= count) break;
        count +=1;
    }
    //printf("MAX: %d, LEFTOVER DIST: %d\n", count, dist);
    int ans = count;
    if(dist > count+1)  count+=2;
    if (dist == count) count-=1;
    else if (dist > 0 && dist <= count+1)  count+=1;
    else if(dist <= (-1)*count)count-=1;
    return ans+count;
}


int main(void){

    int count;
    scanf("%d", &count);
    for(int i = 0; i<count; i++){
        int x, y;
        scanf("%d%d", &x, &y);
        printf("%d\n", route(x, y));
    }
}