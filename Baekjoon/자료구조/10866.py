# 덱
import sys
deque = []

for _ in range(int(input())):
    x = sys.stdin.readline().split()
    if x[0] =='push_front':
        deque.insert(0,x[1])
    elif x[0]=='push_back':
        deque.append(x[1])
    elif x[0]=='pop_front':
        if deque:
            print(deque.pop(0))
        else:
            print(-1)
    elif x[0]=='pop_back':
        if deque:
            print(deque.pop(-1))
        else:
            print(-1)
    elif x[0]=='size':
        print(len(deque))
    elif x[0]=='empty':
        if not deque:
            print(1)
        else:
            print(0)
    elif x[0]=='front':
        if deque:
            print(deque[0])
        else:
            print(-1)
    elif x[0]=='back':
        if deque:
            print(deque[-1])
        else:
            print(-1)

