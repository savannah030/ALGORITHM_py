def solution(clothes):
    dic = dict()
    for [name,type] in clothes:
        if type in dic:
            names = dic.get(type)
            names.add(name)
            dic[type]=names
        else:
            dic[type] = set([name])

    answer = 1
    for values in dic.values():
        answer *= (len(values)+1)
    return answer-1