import sys
input = sys.stdin.readline

zero = [0]*41
one = [0]*41

zero[0],one[0]=1,0
zero[1],one[1]=0,1
for num in range(2,41):
    zero[num]=zero[num-1]+zero[num-2]
    one[num]=one[num-1]+one[num-2]

T = int(input())
for _ in range(T):
    N = int(input())
    print(str(zero[N])+" "+str(one[N]))
    