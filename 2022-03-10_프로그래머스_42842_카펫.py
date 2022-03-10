# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42842

# brown, yellow 로 가로, 세로 길이구하는 건 어렵지만,
# 반대로 가로,세로 길이에서 갈색,노란색칸의 개수는 구하는 건 쉽다.
# yellow = (width-2)*(height-2)
# brown = width*height-(width-2)*(height-2)
# 따라서 가로,세로 각각을 brown과 yellow에 관한 식으로 표현하였다.

def solution(brown,yellow):
    k = int(((brown-4)**2-16*yellow)**0.5)
    return [int((brown+4+k)/4),int((brown+4-k)/4)]