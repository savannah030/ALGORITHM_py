import sys
from itertools import combinations
input = sys.stdin.readline

results = []
for _ in range(4):
    result = list(map(int,input().split()))
    results.append([result[3*i:3*i+3] for i in range(6)])
'''
for i in range(len(results)):
    print(results[i])  
'''
'''
[[5, 0, 0], [3, 0, 2], [2, 0, 3], [0, 0, 5], [4, 0, 1], [1, 0, 4]]
[[4, 1, 0], [3, 0, 2], [4, 1, 0], [1, 1, 3], [0, 0, 5], [1, 1, 3]]
[[5, 0, 0], [4, 0, 1], [2, 2, 1], [2, 0, 3], [1, 0, 4], [0, 0, 5]]
[[5, 0, 0], [3, 1, 1], [2, 1, 2], [2, 0, 3], [0, 0, 5], [1, 0, 4]]
''' 

def back(case,idx):
    
    global matches
    
    if idx==15:
        if sum(map(sum,results[case]))==0: ###### result값이 모두 0이 되어야함
            answers[case]=1
        return 
    
    team1,team2 = matches[idx]
 
    # 팀1이 이긴 경우
    if results[case][team1][0]>0 and results[case][team2][2]>0:
        results[case][team1][0] -= 1
        results[case][team2][2] -= 1
        back(case,idx+1)
        results[case][team1][0] += 1
        results[case][team2][2] += 1
        
    # 비긴 경우
    if results[case][team1][1]>0 and results[case][team2][1]>0:
        results[case][team1][1] -= 1
        results[case][team2][1] -= 1
        back(case,idx+1)
        results[case][team1][1] += 1
        results[case][team2][1] += 1
        
    # 팀1이 진 경우
    if results[case][team1][2]>0 and results[case][team2][0]>0:
        results[case][team1][2] -= 1
        results[case][team2][0] -= 1
        back(case,idx+1)
        results[case][team1][2] += 1
        results[case][team2][0] += 1
   
    
        
matches = list(combinations(range(6),2)) ### 모든 매치 만들기
answers = [0,0,0,0]
for case in range(4): 
    back(case,0)
for i in range(4):
    print(answers[i],end=' ')


