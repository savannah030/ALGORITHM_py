import sys
input = sys.stdin.readline

N = int(input()) # 크레인의 수
cranes = list(map(int,input().split()))
cranes.sort(reverse=True)
#print("cranes=",cranes)

M = int(input()) # 박스의 수
boxes = list(map(int,input().split()))
boxes.sort(reverse=True)
#print("boxes=",boxes)

if cranes[0]<boxes[0]:
    print(-1)
        
else: 
    cnt = 0
    l1,l2 = len(boxes),len(cranes)
    check = [False]*l1
    indices = [0]*l2
    time = 0
    while cnt<l1:
        time += 1
        #print("time=",time)
        for c in range(l2):
            for b in range(indices[c],l1):
                if check[b] or boxes[b]>cranes[c]:
                    indices[c] += 1
                else:
                    check[b]=True
                    cnt += 1
                    #print("crane:",c,"box",boxes[b],"cnt")
                    break
    print(time)
    
    

    