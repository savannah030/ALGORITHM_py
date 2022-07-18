# 12분

def solution(board, moves):
    answer = 0
    l = len(board)
    queue = [-1]
    for move in moves:
        for x in range(l):
            if board[x][move-1]!=0:
                if queue[-1]==board[x][move-1]:
                    answer += 2
                    queue.pop()
                else:
                    queue.append(board[x][move-1])
                board[x][move-1]=0 
                break #####
    
    return answer