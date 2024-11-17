def solution(bin1, bin2):
    answer = ''
    bin1 = int(bin1,2)
    bin2 = int(bin2,2)
    num = bin(bin1 + bin2)
    return num.replace("0b",'')