import sys
import heapq
min_heap = []

for _ in range(int(input())):
    x = sys.stdin.readline().split()

    if int(x[0]) == 0:
        if min_heap:
            print(heapq.heappop(min_heap))
        else:
            print(0)
    else:
        heapq.heappush(min_heap,int(x[0]))
