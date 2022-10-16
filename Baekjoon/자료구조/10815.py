# 숫자 카드 
import sys

N = int(input())
card = sys.stdin.readline().split()
M = int(input())
check = sys.stdin.readline().split()

card.sort()

def binary(arr,target,start,end):
    while start <= end:
        mid = (start+end) //2

        if arr[mid] ==target:
            return mid
        elif arr[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return None

for c in check:
    if binary(card,c,0,N-1) is not None:
        print(1,end=' ')
    else:
        print(0,end=' ')