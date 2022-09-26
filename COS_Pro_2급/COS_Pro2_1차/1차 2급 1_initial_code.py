shirt_size = ["XS", "S", "L", "L", "XL", "S"]

def solution(shirt_size):  
    answer = []
    check = {"XS":0,"S":0,"M":0,"L":0,"XL":0,"XXL":0}
    for i in shirt_size:
        for j in check.keys():
            if i == j:
                check[j]+=1
    for i in check.values():
        answer.append(i)
    return answer
        


ret = solution(shirt_size);
print(ret)