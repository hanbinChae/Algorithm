price = 96900
grade = "S"

def solution(price,grade):
    answer = price
    membership = {"S":5/100,"G":10/100,"V":15/100}
    for m in membership.keys():
        if grade == m:
            price *= membership[m]
            answer -= price
    return int(answer)

ret = solution(price,grade);
print(ret)
