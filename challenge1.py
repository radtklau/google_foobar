def solution(i):
    prime_string = "2"
    natural_number = 2
    
    while(len(prime_string) < i+5):
        prime_number = 0
        len_prime_string = len(prime_string)
        while(len_prime_string == len(prime_string)):
            natural_number += 1
            for denominator in range(natural_number-1,1,-1):
                if(natural_number % denominator == 0):
                    break
                if(denominator == 2):
                    prime_number = natural_number
                    prime_string += str(prime_number)
                    
    return prime_string[i:i+5]

print(solution(9999))