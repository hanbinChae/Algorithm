# 큐, 내가 작성한 답 (시간 초과)
queue = [i for i in range(1,int(input())+1)]

while len(queue)>1:
    queue.pop(0) 
    queue.append(queue.pop(0))
print(queue[0])

# 공식을 이용한 풀이
a = int(input())
b = 2
while True:
    if a == 1 or a == 2:
        print(a)
        break
    b *= 2
    if b >= a:
        print((a - (b // 2)) * 2)
        break