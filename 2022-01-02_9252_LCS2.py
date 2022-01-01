import sys
input = sys.stdin.readline

s1 = '0'+input().rstrip()
s2 = '0'+input().rstrip()

l1,l2 = len(s1),len(s2)

c = [ [""]*l2 for _ in range(l1) ]

for i in range(l1-1):
    for j in range(l2-1):
        if s1[i+1]==s2[j+1]:
            c[i+1][j+1] = c[i][j]+s1[i+1]
        elif len(c[i][j+1])>=len(c[i+1][j]):
            c[i+1][j+1] = c[i][j+1] 
        else: #s1[i]<s2[j]
            c[i+1][j+1] = c[i+1][j]

print(len(c[-1][-1]))  
print(c[-1][-1])    