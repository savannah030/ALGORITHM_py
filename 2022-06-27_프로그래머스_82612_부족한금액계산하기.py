# 3분
def solution(price, money, count):
    need = price*count*(count+1)//2
    if money-need>=0: return 0
    else:
        return need-money