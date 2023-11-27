#include <stdio.h>
// #include <stdlib.h>


int main()
{
    int n, m ;
    
    float result;
    scanf_s(" %c", &C);
    for (char i = 0; i < C; i++)
    {
        scanf_s(" %c", &stuNum);
        printf("%.3f%%", avgfunc(stuNum));
    }
}

// n, m = map(int, input().split())

// li = list(map(int, input().split()))

// dp = [0] * n
// dp[0] = li[0]
// for i in range(1,n):
//     dp[i] = dp[i-1] + li[i]
        
// for _ in range(m):
//     i, j = map(int, input().split())
//     if i == 1:
//         print(dp[j-1])
//     else:
//         print(dp[j-1]-dp[i-2])