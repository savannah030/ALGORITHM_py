# 19분
from collections import defaultdict

def solution(id_list, report, k):
    dic1 = defaultdict(set) # dic1[신고한사람]=신고당한사람
    dic2 = defaultdict(set) # dic2[신고당한사람]=신고한사람
    
    for r in report:
        p1,p2 = r.split()
        dic1[p1].add(p2)
        dic2[p2].add(p1)
    
    suspend = set()
    for p in dic2.keys():
        if len(dic2[p])>=k:
            suspend.add(p)
            
    answer = [0]*len(id_list)
    for s in suspend:
        for p in dic1.keys(): #dic1.keys() id_list랑 순서 같지 않으므로 enumerate 쓰면 안됨
            if s in dic1[p]:
                answer[id_list.index(p)]+=1
    
    return answer