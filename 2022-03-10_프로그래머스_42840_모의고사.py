def solution(answers):
    l = len(answers) # 최대 10000문제
    # 반복되는 패턴
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    
    s1 = p1*(l//5)+p1[:l%5]
    s2 = p2*(l//8)+p2[:l%8]
    s3 = p3*(l//10)+p3[:l%10]
   
    corrects = [0,0,0] # 수포자들이 맞힌 문제의 개수
    for i in range(l):
        if s1[i]==answers[i]:
            corrects[0] += 1
        if s2[i]==answers[i]:
            corrects[1] += 1
        if s3[i]==answers[i]:
            corrects[2] += 1
    '''
    MAX = max(corrects) # 가장 많이 맞힌 사람이 맞힌 문제의 개수
    answer = []
    for i in range(3):
        if corrects[i]==MAX:
            answer.append(i+1)
    '''
            
    return [i+1 for i in range(3) if corrects[i]==max(corrects)]