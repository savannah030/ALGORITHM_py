import sys
input = sys.stdin.readline

L,C = map(int,input().split())
cand = list(input().split())
cand.sort() 

consonant = 0 # 자음의 수
vowel = 0 # 모음의 수
def back(password, _consonant, _vowel, idx):

    # 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음
    if len(password)==L and _consonant>=2 and _vowel>=1: 
        print(password)
        return
        
    for i in range(idx,C):
        if cand[i] in "aeiou": # 모음이면
            back(password+cand[i], _consonant, _vowel+1, i+1)
        else: # 자음이면
            back(password+cand[i], _consonant+1, _vowel, i+1)

back("",0,0,0)