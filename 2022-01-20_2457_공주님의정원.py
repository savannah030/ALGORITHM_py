import sys
input = sys.stdin.readline

N = int(input()) #꽃개수<=100,000
'''
예를 들어, 한 줄 입력이 1 1 5 31 로 들어오면
flowers.append((101,531)) 로 저장
'''
flowers = []
for _ in range(N):
    date = list(map(int,input().split()))
    st,en = date[0]*100+date[1],date[2]*100+date[3]
    flowers.append((st,en))
flowers.sort()

end,tmp,idx,ans = 301,301,0,0
while end<=1130:
    # 겹치는 꽃들 중 가장 늦게 지는 꽃 고르기
    # tmp가 갱신되지 못하는 꽃은 다음 번에도 볼 필요없기 때문에
    # idx += 1 해줘도 됨
    while idx<N and flowers[idx][0]<=end:
        tmp = max(tmp,flowers[idx][1])
        idx += 1
    # 겹치는 꽃이 없으면
    if tmp==end:
        print(0)
        sys.exit(0)
    end = tmp
    ans += 1
print(ans)