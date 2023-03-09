import challenge2_2
import challenge_test
import random
import time

inp = []
a = 0

while True:
    length = random.randint(2,21)
    if random.randint(1,100) == 50:
        inp.append(1)
    while len(inp) < length:
        t = random.randint(1,10000)
        if t > a:
            inp.append(t)
            if t > 9995 and len(inp) >= 2:
                break
            a = t
            if random.randint(1,100) == 50:
                inp.append(10000)
                break
    print("_________________")
    print(inp)
    ans1 = challenge2_2.solution(inp)
    ans2 = challenge_test.answer(inp)
    print(ans1)
    print(ans2)
    if(ans1 != ans2):
        break
    inp = []
    t = 0
    a = 0
    #time.sleep(0.1)