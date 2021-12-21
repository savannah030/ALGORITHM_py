import sys
from itertools import combinations
input = sys.stdin.readline

N,K = map(int,input().split()) # 1<=N<=60 0<=K<=26
K -= 5
if K<0:
    print(0)
else:  
    s1 = set()#d = dict() # d[a] = a글자가있는단어의개수
    s2 = {'a','c','i','n','t'}

    check = [ [0]*26 for _ in range(N) ]
    for i in range(N): # 단어길이 8~15, 중복 X
        word = set(input().rstrip()[4:-4])-s2
        for w in word:
            check[i][ord(w)-97]=1
        s1.update(word)

    if K>=len(s1):
        print(N)
    else:
        ans = 0
        for letters in combinations(s1,K):
            tmp = 0
            check0 = [ check[i][:] for i in range(N) ]
            for letter in letters:
                for i in range(N):
                    if check0[i][ord(letter)-97]==1:
                        check0[i][ord(letter)-97]=0

            for i in range(N):
                if sum(check0[i])==0:
                    tmp += 1
            
            ans = max(ans,tmp)
    
        print(ans)
        
    
                
                
        
            
            
    
    
