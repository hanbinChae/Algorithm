import sys
stack = []
result = 0

for _ in range(int(input())):
    x = sys.stdin.readline().split()
    if int(x[0]) == 0:
        stack.pop(-1)
    else:
        stack.append(int(x[0]))

for s in stack:
    result+=s
print(result)
     