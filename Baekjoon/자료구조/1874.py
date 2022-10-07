# 스택 수열
import sys
answer = []
stack = []
flag = 0
cur = 1
for _ in range(int(input())):
    x = sys.stdin.readline().split()
    while cur <= x:
        stack.append(cur)
        answer.append("+")
        cur+=1
    
    if stack[-1]==x:
        stack.pop()
        answer.append("-")
    else:
        print("NO")
        flag = 1
        break;

if flag == 0:
    for a in answer:
        print(a)