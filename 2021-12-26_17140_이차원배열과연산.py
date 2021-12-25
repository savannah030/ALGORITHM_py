import sys
input = sys.stdin.readline

r,c,k = map(int,input().split())
r -= 1
c -= 1
# 배열의 인덱스는 1부터 시작
A = []
for _ in range(3):
    A.append(list(map(int,input().split())))
    
def calculate(board):
    MAX = 0
    for x in range(len(board)):
        freq = [0]*(max(board[x])+1)
        for y in range(len(board[x])):
            freq[board[x][y]] += 1
        tmp = []
        for i in range(1,len(freq)):
            if freq[i]==0: continue
            tmp.append((i,freq[i]))
        tmp = sorted(tmp, key=lambda x:(x[1],x[0])) # 수의 등장 횟수가 커지는 순으로, 그러한 것이 여러가지면 수가 커지는 순으로 정렬
        li = []
        for t in tmp:
            li += [t[0],t[1]]
        MAX = max(len(li),MAX)
        board[x] = li[:100] # 처음 100개를 제외한 나머지는 버린다
        
    if MAX>100: MAX=100
    for x in range(len(board)):
        board[x] += [0]*(MAX-len(board[x]))
        
    return board
    
time = 0
while time<=100:
    
    if len(A)>r and len(A[0])>c: ######## len(A)<r and len(A[0])<c 라고 써서 디버깅 오래했음..
        if A[r][c]==k:
            print(time)
            sys.exit(0)
    
    if len(A)>=len(A[0]): # 행>=열
        # R 연산(행에 대해서 정렬수행)
        A = calculate(A)
            
    else: 
        # C 연산 (배열 90도 회전해서 calculate함수 쓴다음에 다시 되돌리는 방법 사용)
        A_rotate = zip(*A)
        A_rotate = [list(a_r) for a_r in A_rotate]
        
        A = calculate(A_rotate)
        
        ## 다시 원래대로 되돌리기
        A_rotate = zip(*A)
        A_rotate = [list(a_r) for a_r in A_rotate]
    
        # A = deepcopy(A_rotate)
        A = []       
        A = [A_rotate[i][:] for i in range(len(A_rotate))]
          
    time += 1
        
        
print(-1)