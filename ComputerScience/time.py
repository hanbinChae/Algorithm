import time
start = time.time()
score = [70,60,50,80,90,40]
max = score[0]

for i in score:
    if max <i:
        max = i;
print(max)
print("Time:",time.time()-start)
