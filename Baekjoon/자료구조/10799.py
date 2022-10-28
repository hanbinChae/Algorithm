# 쇠막대기

bar_size = list(input())
stack = []
result = 0

for i in range(len(bar_size)):
    if bar_size[i] == '(':
        stack.append('(')
    else:
        if bar_size[i-1] =='(':
            stack.pop()
            result += len(stack)
        else:
            stack.pop()
            result+=1
print(result)
        