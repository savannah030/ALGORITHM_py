# 위치가 음수인 책과 양수인 책을 나눠서
# (M step마다의 위치)*2 더하기 (한번에 들수있는 책이 M권이고, 다시 0으로 돌아와야 하므로)
# 마지막에는 그냥 위치더하기(다시 0으로 돌아올 필요 없으므로)
import sys
input = sys.stdin.readline

N,M = map(int,input().split()) # 책의개수,한번에들수있는수<=50
books = list(map(int,input().split()))
books_l = [ b for b in books if b<0]
books_r = [ b for b in books if b>0]
books_l.sort()
books_r.sort(reverse=True)

l1,l2 = len(books_l),len(books_r)
arr = [abs(books_l[i]) for i in range(0,l1,M)]
arr += [abs(books_r[i]) for i in range(0,l2,M)]
arr.sort()
print(arr.pop()+2*sum(arr))

