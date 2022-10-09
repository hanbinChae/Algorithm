# 요세푸스 문제
N,K  = map(int,input().split())
circle = [i for i in range(1,N+1)]
answer = []
idx = 0

for i in range(N):
    idx += (K-1)
    if idx >= len(circle):
        idx %= len(circle)
    answer.append(str(circle[idx]))
    circle.pop(idx)

print("<",', '.join(answer),'>',sep='')
    


