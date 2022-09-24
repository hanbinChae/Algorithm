from hashlib import new


new_id = "...!@BaT#*..y.abcdefghijklm";

def solution(new_id):
    answer = ''

    id = new_id.lower()
    
    for i in id:
        if i.isalnum() or i in '-_.':
            answer+=i
    
    while ".." in answer:
        answer = answer.replace("..",'.')
    
    if answer[0] == '.' and len(answer) > 1:
        answer = answer[1:]
    if answer[-1] == '.':
        answer = answer[:-1]

    if answer == "":
        answer = 'a'
    
    if len(answer)>15:
        answer= answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    if len(answer) < 3:
        answer = answer + answer[-1] * (3-len(answer))
    print(answer)

    return answer

solution(new_id)