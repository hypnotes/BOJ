#include <stdio.h>

int calculate(int num);
int modify(int arr[], int num, int i);
int calculate(int num){
    //if multiple of 5
    if(num%5==0) return num/5;

    //INITIALIZE
    int arr[5001] = {0,};
    int i = 0;
    if(num >= 5){
        while(num >= 5){
            arr[i] = 5;
            i++;
            num-=5;
        }
    }
    if(num >= 3){
        while(num >=3){
            arr[i] = 3;
            i++;
            num-=3;
        }
    }
    if (num==0) return i;

    //MODIFY
    int ans = modify(arr, num, i-1);
    return ans;
}
int modify(int arr[], int num, int i){
    if(arr[0] == 0) return -1;
    while(arr[i]==3){
        num+=3;
        arr[i] = 0;
        i--;
    }

    if(arr[i]==5){
        num+=5;
        arr[i] = 3;       

        i++;
        num-=3;

        while(num>=3){
            num-=3;
            arr[i]=3;
            i++;
        }

    }
    if(num!=0)  modify(arr, num, i-1);
    if(num == 0) return i;
    
}

int main(void){
    int num;
    scanf("%d", &num);
    printf("%d", calculate(num)); 
}