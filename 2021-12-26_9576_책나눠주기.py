# https://blog.naver.com/ndb796/221240613074 나동빈님 이분매칭 알고리즘 참고
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1005) ## 디폴트값 1000이기 때문에 늘리기!

# 매칭에 성공한 경우 True 실패한 경우 False 
def dfs(now):
    
    global visited,students
    
    for book in students[now]: # now번째 학생이 가질 수 있는 책들 중
        
        if visited[book]: continue # 이미 탐색했으면 더 볼 필요없음
        visited[book]=True
        
        # book을 소유한 사람이 없거나 own[book]이 가질 수 있는 책이 남아있으면
        if own[book]==-1 or dfs(own[book]): 
            own[book]=now
            return True
        
    return False


for case in range(int(input())): 
    N,M = map(int,input().split()) # 총 N권,M명
    students = []

    own = [-1]*N # n번째 책을 m번째 학생이 소유했다면 own[n]=m
    for m in range(M):
        a,b = map(int,input().split())
        students.append([n for n in range(a-1,b)]) # 책 0번부터 시작

    count = 0
    for x in range(len(students)):
        #### for문 돌때마다 visited 초기화해줘야함!!!!
        visited = [False]*N # n번째 책을 확인했다면 visited[n]=True
        if dfs(x): count += 1
        
    '''
    for i in range(len(own)):
        print("student",own[i],"own",i)
    '''
    print(count)
        
    