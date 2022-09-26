#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(cards):
    answer = 0
    color = [0]*len(cards)
    for c in cards:
        if c[0] == "red":
            answer+=int(c[1])
            color[0]+=1
        elif c[0] == "blue":
            answer+=int(c[1])
            color[1]+=1
        elif c[0] == "black":
            answer+=int(c[1])
            color[2]+=1
    if color[0] ==3 or color[1]==3 or color[2] ==3:
        answer *= 3
    elif color[0] ==2 or color[1]==2 or color[2] ==2:
        answer *=2
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
cards1 = [["blue", "2"], ["red", "5"], ["black", "3"]]
ret1 = solution(cards1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

cards2 = [["blue", "2"], ["blue", "5"], ["black", "3"]]
ret2 = solution(cards2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")