#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(people):
    size = {"S":0,"M":0,"L":0,"XL":0}
    answer = [0 for _ in range(4)]
    for each_size in people:
        if each_size < 95:
            size["S"]+=1
        elif 100 > each_size >= 95:
            size["M"]+=1;
        elif 105 > each_size >= 100:
            size["L"]+=1
        else:
            size["XL"]+=1;
    idx = 0
    for s in size.values():
        answer[idx] = s
        idx+=1
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
people = [97, 102, 93, 100, 107]
ret = solution(people)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")