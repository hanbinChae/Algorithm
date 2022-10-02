import sys
# 이분 탐색
n = sys.stdin.readline()
stack = sorted(sys.stdin.readline().split())
m = sys.stdin.readline()
x_list = list(sys.stdin.readline().split())

def binary(x,stack,start,end):
    if start > end:
        return 0
    mid = (start+end)//2
    if x == stack[mid]:
        return 1
    elif x < stack[mid]:
        return binary(x,stack,start,mid-1)
    else:
        return binary(x,stack,mid+1,end)


for x in x_list:
    start = 0
    end = len(stack)-1
    print(binary(x,stack,start,end))
            