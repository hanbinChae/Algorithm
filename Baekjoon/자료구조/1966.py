# 프린터 큐
for _ in range(int(input())):
    cnt = 0
    N,M = map(int,input().split())
    pri = list(map(int,input().split())) 

    m_pri = [0 for i in range(N)]
    m_pri[M] = 1

    while True:
        if pri[0]==max(pri):
            cnt+=1

            if m_pri[0] != 1:
                del pri[0]
                del m_pri[0]
            
            else:
                print(cnt)
                break
        else:
            pri.append(pri.pop(0))
            m_pri.append(m_pri.pop(0))