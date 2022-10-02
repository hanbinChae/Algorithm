# 스택
import sys
stack = []

def pop_(stack):
    if stack:
        return stack.pop()
    else:
        return -1
def empty_(stack):
    if not stack:
        return 1
    else:
        return 0

def top_(stack):
    if stack:
        return (stack[-1])
    else:
        return (-1)

for _ in range(int(input())):
    x = sys.stdin.readline().split() 
    # 입출력 속도 비교 : sys.stdin.readline > raw_input() > input()
    if x[0] == 'push':
        stack.append(x[1])
    elif x[0] =='pop':
        r = pop_(stack)
        print(r)
    elif x[0] == 'size':
        print(len(stack))
    elif x[0] =='empty':
        r = empty_(stack)
        print(r)
    elif x[0] =='top':
        r = top_(stack)
        print(r)
    else:
        pass;     
