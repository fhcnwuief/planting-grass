def solution(array, n):
    answer = 0
    box = []
    array.sort()
    for i in array:
        box.append(abs(n-i))
    #box.index(min(box)) -> box의 최소값의 index 구하는 거
    #array[box.index(min(box))] -> box의 최소값의 index를 array의 index로 활용
    answer = [array[box.index(min(box))]]
    if len(answer) != 0:
        answer = min(answer)
        
    return answer
            