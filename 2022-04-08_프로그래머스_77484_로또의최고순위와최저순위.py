def solution(lottos, win_nums):
    
    erased = 0 # 알아볼 수 없는 번호
    matched = 0 # 로또 번호와 일치하는 번호의 수
    for lotto in lottos:
        if lotto==0:
            erased += 1
        elif lotto in win_nums:
            matched += 1
    highest,lowest = 7-matched-erased,7-matched
    if highest<1:
        highest = 1
    elif highest>6:
        highest = 6
    if lowest<1:
        lowest = 1
    elif lowest>6:
        lowest = 6
    return [highest,lowest] 