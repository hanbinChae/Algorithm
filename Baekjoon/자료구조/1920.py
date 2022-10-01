import sys
# 미완
temp = int(input())
stack = list(sys.stdin.readline().split())
temp2 = int(input())
x_list = list(sys.stdin.readline().split())

for i in range(temp2):
    if x_list[i] in stack:
        print(1)
    else:
        print(0)
            