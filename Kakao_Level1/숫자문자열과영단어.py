s = ["one4seveneight","23four5six7","2three45sixseven","123"]
def solution(s):
        s = s.replace('zero','0')
        s = s.replace('one','1')
        s = s.replace('two',"2")
        s = s.replace('three',"3")
        s = s.replace('four',"4")
        s = s.replace('five',"5")
        s = s.replace('six',"6")
        s = s.replace('seven',"7")
        s = s.replace('eight',"8")
        s = s.replace('nine','9')
        
        answer = int(s)
        return answer
idx = 1
for i in s:
    result  = solution(i)
    print(f"{idx}번",result)
    idx+=1