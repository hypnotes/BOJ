import sys 
from collections import deque 

a = sys.stdin.readline()[:-1]
st = deque()
for i in range(len(a)):
    
    if len(st) > 2 and a[i] == 'P' and st[-1] == 'A' and st[-2] == 'P' and st[-3] == 'P':
        st.pop()
        st.pop()
        st.pop()
        
    st.append(a[i])
    
print('PPAP') if len(st) == 1 and st[0] == 'P' else print('NP')        