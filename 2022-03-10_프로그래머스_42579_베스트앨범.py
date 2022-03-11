def solution(genres, plays):
    
    l = len(genres)
    dic = dict()
    '''
    dic = {
        genre : [ (고유번호, 재생횟수), ...],
    }
    '''
    # 최대 10,000번 반복
    for i in range(l):
        if genres[i] in dic:            # dic = {key: value} 에서 key로 genres[i]가 있으면
            li = dic.get(genres[i])
            li.append((i,plays[i]))     # 기존 value에 새로운 (고유번호, 재생횟수) 추가하고
            dic[genres[i]] = li         # dic[key] 갱신
        else:
            dic[genres[i]] = [ (i,plays[i]) ]

    # 장르 내에서 곡 정렬
    for (key,value) in dic.items(): # key = 'classic', value = [(0, 500), (2, 150), (3, 800)]
        # 조건 2: 많이 재생된 순으로, 조건 3: 재생횟수가 같으면 고유번호가 낮은 순으로 
        dic[key] = sorted(value, key=lambda x:(-x[1],x[0])) # 정렬된 value로 갱신

    # 조건 1: 속한 노래가 많이 재생된 순으로 장르 정렬
    srt_genres = sorted(dic.keys(), key=lambda k: -sum(song[1] for song in dic[k]) )  # dic[k]=[(0, 500), (3, 500), (2, 150)]
    # srt_genres = ['pop', 'classic']

    answer = []
    for genre in srt_genres:
        # 장르별로 가장 많이 재생된 두 노래를 추가([:2]는 배열의 길이가 1이라면 알아서 [:1]까지만 포함)
        answer.extend([song[0] for song in dic[genre][:2]])

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop", "rnb"], [500, 600, 150, 500, 2500, 300]))
# [4, 1, 3, 0]