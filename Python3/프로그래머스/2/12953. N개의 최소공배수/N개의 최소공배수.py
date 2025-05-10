def solution(arr):
    a = arr[0]
    for idx in range(len(arr)-1):
        b = arr[idx+1]
        for x in range(max(a,b),(a*b)+1):
            if x%a == 0 and x%b == 0:
                a = x
                break            
    return a