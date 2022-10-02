# VPS 검사, 스택
for _ in range(int(input())):
    x = list(input())
    stack = []
    for each_x in x:
        if each_x =='(':
            stack.append(each_x)
        elif each_x == ')':
            if stack:
                stack.pop()
            else:
                print("NO")
                break;
    else:
        if not stack:
            print("YES")
        else:
            print("NO")

