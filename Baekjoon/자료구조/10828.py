stack = []

for _ in range(int(input())):
    x = input()
    if 'push' in x:
        stack.append(x[-1])
    elif 'pop' in x:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif 'size' in x:
        print(len(stack))
    elif 'empty' in x:
        if not stack:
            print(1)
        else:
            print(0)
    elif 'top' in x:
        if stack:
            print(stack[-1])
        else:
            print(-1)
