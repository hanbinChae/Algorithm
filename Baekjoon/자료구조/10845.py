# 큐 Queue
import sys
queue = []

def push_(x):
    queue.append(x)
def pop_():
    if queue:
        print(queue.pop(0))
    else:
        print(-1)

for _ in range(int(input())):
    x = sys.stdin.readline().split()
    if x[0]=='push':
        push_(x[1])
    elif x[0]=='pop':
        pop_()
    elif x[0]=='size':
        print(len(queue))
    elif x[0]=='empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif x[0]=='front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif x[0]=='back':
        if queue:
            print(queue[-1])
        else:
            print(-1)

