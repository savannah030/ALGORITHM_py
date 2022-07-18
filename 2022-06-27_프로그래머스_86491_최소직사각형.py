# 12분
def solution(sizes):
    
    for i in range(len(sizes)):
        if sizes[i][0]>sizes[i][1]:
            sizes[i][0],sizes[i][1] = sizes[i][1],sizes[i][0]
    
    lengths = list(zip(*sizes))
    return max(lengths[0])*max(lengths[1])