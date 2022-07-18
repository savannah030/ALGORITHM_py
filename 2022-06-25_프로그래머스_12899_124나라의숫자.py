# https://velog.io/@syhwang4223/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-124-%EB%82%98%EB%9D%BC%EC%9D%98-%EC%88%AB%EC%9E%90

def solution(n):
    num = ['1','2','4']
    answer = ""

    # 나머지가 0으로 떨어지는 경우가 있으면 몫을 하나 낮추어서 나머지가 3이 되도록 해주어야합니다.
    while n > 0:
        n -= 1 # 나머지 012 대신 123으로 만듦(인덱스) 예) 9=3*3+0이 아니라 2*3+3이 되도록 (몫을 낮추어서 나머지가 0이 되지 않도록)
        answer = num[n % 3] + answer
        n //= 3

    return answer