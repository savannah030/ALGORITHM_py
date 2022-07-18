# from heapq import heappush,heappop,heapify
from itertools import permutations

# 던전 8개밖에 안되므로 완전탐색하기!! 8!~=4만
def solution(k, dungeons):
    answer = 0 
    for per in permutations(dungeons,len(dungeons)):
        k_cp = k
        tmp = 0
        # ["최소 필요 피로도", "소모 피로도"]
        for dungeon in per:
            if k_cp<dungeon[0]: break
            k_cp -= dungeon[1]
            tmp += 1
        answer = max(tmp,answer)
        
    return answer

'''
# 24분
def wrong1(k, dungeons):
    # 시도 1
    # ["최소 필요 피로도", "소모 피로도"]
    # 최소 필요 피로도가 큰 순으로 정렬
    # 하나씩 힙에 넣을 때
    # 현재 피로도가 최소 필요 피로도보다 작으면 
    # 힙에 있는 던전 중 소모 피로도가 가장 큰 애 빼기 -> 얘 다시 dungeons에 넣기 까다로움 (컵라면 문제st 아님)
    dungeons = sorted(dungeons,key=lambda x:-x[0])
    q = []
    for dun in dungeons:
        if k<dun[0]:
            k -= heappop(q)[0] # 소모된 피로도 다시 더하기
            print("복구 k=",k)
        k -= dun[1]
        heappush(q,(-dun[1],dun[0]))
        print("dun=",dun)
        print("k=",k)
    return len(q)

def wrong2(k, dungeons):
    
    # ["최소 필요 피로도", "소모 피로도"] 
    # 현재 갈 수 있는 던전 중 가장 소모 피로도가 작은 애 고르기 xxx
    
    #dugeons = sorted(dugeons, key=lambda x:x[0]) # 최소 필요 피로도 작은 순으로 정렬
    heapify(dungeons)
    
    answer = 0 
 
    while dungeons:
        able = []
        while dungeons and dungeons[0][0]<=k:
            need,consume = heappop(dungeons)
            heappush(able,(consume,need))
        print("able=",able)
        if able:
            consume,need = heappop(able)
            k -= consume
            dungeons += [(a[1],a[0]) for a in able]
            heapify(dungeons)
            print("dungeons=",dungeons)
            answer += 1
        else: break
    
    return answer
'''
print(solution(80,[[80,20],[50,40],[30,10]])) # 3