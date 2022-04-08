# 23분 한번에 성공
def solution(rows, columns, queries):
    board = [ [i*columns+j+1 for j in range(columns)] for i in range(rows)]
    '''
    for i in range(rows):
        print(board[i])
    '''
    answer = []
    for query in queries:
        x1,y1,x2,y2 = [q-1 for q in query] #[1,1,4,3]
        newboard = [ b[:] for b in board ]
        MIN = 10001
        # 동
        for j in range(y1,y2):
            newboard[x1][j+1]=board[x1][j]
            MIN = min(MIN,board[x1][j])
        # 남
        for i in range(x1,x2):
            newboard[i+1][y2]=board[i][y2]
            MIN = min(MIN,board[i][y2])
        # 서
        for j in range(y2,y1,-1):
            newboard[x2][j-1]=board[x2][j]
            MIN = min(MIN,board[x2][j])
        # 북
        for i in range(x2,x1,-1):
            newboard[i-1][y1]=board[i][y1]
            MIN = min(MIN,board[i][y1])
        
        board = [ nb[:] for nb in newboard ]
        '''
        print("query=",query)
        for i in range(rows):
            print(board[i])
        '''
        answer.append(MIN)
    
    return answer