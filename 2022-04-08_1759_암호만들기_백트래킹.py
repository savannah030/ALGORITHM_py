import sys
input = sys.stdin.readline

L,C = map(int,input().split())
letters = list(input().split())
letters.sort()
#print(letters) # ['a', 'c', 'i', 's', 't', 'w']

def back(password,idx,consonant,vowel):
    
    # 마지막 글자까지 탐색했으면 리턴
    if idx==C: return
    
    # letter[idx]가 자음인지 모음인지 검사
    if letters[idx] in "aeiou":
        vowel += 1
    else:
        consonant += 1
    password += letters[idx]
    
    # L글자 다 만들었으면 조건에 맞는지 검사하고 출력
    if consonant+vowel==L:
        if consonant>=2 and vowel>=1:
            print(password)
        return
    
    #### 현재 인덱스의 다음부터 C까지 모두 검사해야함!!!!
    for nxtidx in range(idx+1,C):
        back(password,nxtidx,consonant,vowel)
    
for idx in range(0,C-L+1):
    back("",idx,0,0)