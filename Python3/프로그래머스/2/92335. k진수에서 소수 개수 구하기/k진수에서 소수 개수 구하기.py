import math

def solution(n, k):
    answer = 0
    rev_base = ''
    
    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)

    number = rev_base[::-1].split("0")
    number = [v for v in number if v]
    
    for num in number:
        if int(num) != 1 and is_prime_num(int(num)):
            answer += 1
    return answer


def is_prime_num(n):
    for i in range(2, int(math.sqrt(n))+1): 
        if n % i == 0:
            return False

    return True