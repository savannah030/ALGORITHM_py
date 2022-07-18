# 1시간 20분... (좌표변환이랑 예외처리 오래걸림)

def solution(lines):
    
    points = []
    for i in range(len(lines)):
        for j in range(i+1,len(lines)):
            A,B,C = lines[i]
            a,b,c = lines[j]
            # 평행하면 패스
            if A*b==a*B: continue
            x = (B*c-b*C)/(A*b-a*B) 
            y = (a*C-A*c)/(A*b-a*B) #######
            if int(x)==x and int(y)==y:
                points.append((int(x),int(y))) 
                
    zipped = list(zip(*points))
    
    MINx,MINy = min(zipped[0]),min(zipped[1])
    MAXy = max(zipped[1])-MINy
    
    newPoints = []
    for i in range(len(points)):
        xx,yy = points[i][0]-MINx,points[i][1]-MINy
        xxx,yyy =  MAXy-yy,xx
        newPoints.append((xxx,yyy))

    zipped2 = list(zip(*newPoints))
    answer = [ ['.']*(max(zipped2[1])+1) for _ in range(max(zipped2[0])+1) ]
  
    for p in newPoints:
        answer[p[0]][p[1]]='*'
  
    return [''.join(a) for a in answer]