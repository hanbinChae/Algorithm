import sys
input = sys.stdin.readline

while True:
    str_list = input().rstrip()
    stack = []
    flag = 1

    for s in str_list:
        if s =='(' or s=='[':
            stack.append(s) #스택 안에 삽입

        elif s ==')':
            if stack and stack[-1]=='(': #스택 마지막 값이 '('일 경우 참
                stack.pop()
            else:
                flag = 0
                break;
        elif s ==']':
            if stack and stack[-1] =='[':
                stack.pop()
            else:
                flag = 0
                break;
                
    if str_list =='.':
        print('yes')
        break;

    print('yes' if flag and not stack else 'no')

