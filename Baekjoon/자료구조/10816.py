# 숫자 카드 2
import sys
from collections import Counter

_ = int(input())
N = sys.stdin.readline().split()
_ = int(input())
M = sys.stdin.readline().split()

C = Counter(N) #n의 개수를 센 Dic 반환
print(" ".join(f"{C[m]}" if m in C else '0' for m in M))
