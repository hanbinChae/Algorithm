N,M = map(int,input().split())

name = set()
compare = set()

for _ in range(N):
    name.add(input())

for _ in range(M):
    compare.add(input())

result = sorted(list(name&compare))

print(len(result))
for r in result:
    print(r)
