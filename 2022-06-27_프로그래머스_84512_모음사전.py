# 13분 문제 잘 읽기..
# 중복허용,순서있음 -> product 사용?
from itertools import combinations_with_replacement
from itertools import permutations

def solution(word):
    dic1 = set()
    for l in range(1,6):
        for com in combinations_with_replacement("AEIOU",l): 
            for per in permutations(com,l):
                dic1.add("".join(per))
                         
    dic2 = sorted(dic1)
    return dic2.index(word)+1