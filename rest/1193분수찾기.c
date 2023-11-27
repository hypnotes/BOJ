#include <stdio.h>

int arr[10020000][2];

int main(void){

    int inp;
    scanf("%d", &inp);

    arr[0][0] = 1;
    arr[0][1] = 1;
    int increase = 1;
    int count = 1;
    while(count < inp ){
        
        for(int i = 0; i<increase; i++){
            if (increase%2==1){ //if odd
                arr[count][0] = arr[count-1][0] -1;
                arr[count][1] = arr[count-1][1] +1;
                if(arr[count][0]==0) arr[count][0] = 1;
                if(arr[count][1]==0) arr[count][1] = 1;
            }
            else{
                arr[count][0] = arr[count-1][0] +1;
                arr[count][1] = arr[count-1][1] -1;
                if(arr[count][0]==0) arr[count][0] = 1;
                if(arr[count][1]==0) arr[count][1] = 1;
            }
            //printf("%d/%d ", arr[count][0], arr[count][1]);
            count ++;
        } 
        increase++;
    }
    printf("%d/%d ", arr[inp-1][0], arr[inp-1][1]);
}