set = [1,1,2,2,2,8]

x = list(map(int,input().split()))
result= []

for i in range(len(x)):
    if set[i] == x[i]:
        result.append(0)
    else:
        if set[i] > x[i]:
            result.append(set[i]-x[i])
        if set[i] < x[i]:
            result.append(set[i]-x[i])

for r in result:
    print(r,end=" ")