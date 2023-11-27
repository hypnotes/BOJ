dp = [0]*5001
dp[0], dp[1] = 1, 1,

a = input()
a = ' '+a
if a[1]!= '0':
   for i in range(2, len(a)):
      if a[i] != '0':
         dp[i] += dp[i-1]% 1000000
      if a[i-1] == '1' or a[i-1]=='2' and a[i] <= '6':
         dp[i] += dp[i-2] %1000000 

   print(dp[len(a)-1]%1000000)
else:
   print(0)