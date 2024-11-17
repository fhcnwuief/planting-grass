def solution(numbers, k):
    answer = 0
    #인덱스 값으로 직접 구하려 하지말고, 리스트를 확장 시키면 됨
    if len(numbers) < k * 2:
        #리스트 확장
        numbers = numbers * ((k*2) // len(numbers) + 1)

    answer = numbers[2*(k-1)]
    return answer