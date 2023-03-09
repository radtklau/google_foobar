def xor(a, b):
    if(a%2==0):
        xor_rotation = [b, 1, b+1, 0]
    else:
        xor_rotation= [a, a^b, a-1, (a-1)^b]
    return xor_rotation[(b-a)%4]

def solution(start, length):
    res=0
    for i in range(0, length):
        res ^= xor(start+(length*i), start+(length*i)+(length-i)-1)
    return res

