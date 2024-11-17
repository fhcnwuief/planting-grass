def solution(a, b, c, d):
    arr = [a, b, c, d]
    arr1 = list(set(arr))

    if len(arr1) == 1:
        return 1111 * arr1[0]
    elif len(arr1) == 2:
        for p in arr1:
            if arr.count(p) == 3:
                q = [q for q in arr1 if q != p][0]
                return (10 * p + q) ** 2
            elif arr.count(p) == 2:
                q = [q for q in arr1 if q != p][0]
                return (p + q) * abs(p - q)
    elif len(arr1) == 3:
        for num in arr1:
            if arr.count(num) == 2:
                arr1.remove(num)
                return arr1[0] * arr1[1]
    else:
        return min(arr1)