#다음과 같이 import를 사용할 수 있습니다.
#import math

from audioop import reverse


def solution(score):
    answer = []
    for idx_s in range(len(score)):
        rank=1
        for each_s in score:
            if score[idx_s] < each_s:
                rank+=1
        answer.append(rank)
            
            # elif answer[idx_s] == answer[idx_s+1]:
            #     answer[idx_s-1] = answer[idx_s]
                
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
score1 = [90, 87, 87, 23, 35, 28, 12, 46]
ret1 = solution(score1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret1, " 입니다.")

score2 = [10, 20, 20, 30]
ret2 = solution(score2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret2, " 입니다.")