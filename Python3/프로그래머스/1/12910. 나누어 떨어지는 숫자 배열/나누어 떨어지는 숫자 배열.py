def solution(arr, divisor):
    answer = [num for num in arr if num % divisor == 0]
    answer.sort()
    return answer if len(answer) != 0 else [-1]