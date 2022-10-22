import heapq
import sys
max_heap = []

for _ in range(int(input())):
    x = sys.stdin.readline().split()
    
    if int(x[0])==0:
        if max_heap:
            print(-1*heapq.heappop(max_heap))
        else:
            print(0)
    else:
        heapq.heappush(max_heap,-1*int(x[0]))
