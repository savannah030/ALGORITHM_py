import sys
input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()

l1,l2 = len(s1),len(s2)

c = [[0]*(l2+1) for _ in range(l1+1)]

for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i]==s2[j]:
            c[i+1][j+1] = c[i][j]+1
        else:
            c[i+1][j+1] = max(c[i][j+1],c[i+1][j])
            
print(c[-1][-1])
