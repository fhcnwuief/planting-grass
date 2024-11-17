from math import gcd

def solution(a,b):
    # 분모를 최대공약수로 나눔
    b //= gcd(a,b)
    # 2로 나누어 떨어지면(2의 배수이면)
    while b%2 == 0:
        # b를 2로 다시 나눔 -> b가 1이 될 때까지
        b //= 2
    # 5로 나누어 떨어지면(5의 배수)
    while b%5 == 0:
        # b를 5로 다시 나눔 -> b가 1이 될 때까지
        b //= 5
    return 1 if b==1 else 2