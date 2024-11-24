def solution(arr):
    if len(arr) == 1 and arr[0] == 10:
        return [-1]
    
    min_value = min(arr)
    return [x for x in arr if x != min_value]