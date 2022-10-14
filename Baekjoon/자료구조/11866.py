# 요세푸스 문제 0
import sys
input = sys.stdin.readline
N, K = map(int,input().split())

circle = [i for i in range(1,N+1)]
result = []
now = K-1

while circle:
    result.append(circle.pop(now))
    if circle:
        now = ((now-1)+K) % len(circle)
    
print("<",", ".join(str(r) for r in result),'>',sep='')
