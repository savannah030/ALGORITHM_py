import sys
from itertools import combinations
input = sys.stdin.readline

# 0~9 사이의 숫자 중 digit개를 뽑아(combinations 이용) 감소하는 수 만들어 answers에 추가

answers = [] # 감소하는 수

for digit in range(1,11): #9876543210이 최대. 즉 10자리수까지만 가능하므로 1<=digit<=10으로 설정
    for combi in combinations([i for i in range(0,10)], digit):
        answers.append(int(''.join([str(num) for num in sorted(combi, reverse=True)]))) 
answers.sort()

num = int(input())
if num>=len(answers): 
    print(-1)
else:
    print(answers[num])
