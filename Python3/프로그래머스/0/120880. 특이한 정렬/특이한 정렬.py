def solution(numlist, n):
    numlist = sorted(numlist,reverse=True)
    numlist = sorted(numlist,key = lambda x : abs(n-x))
    return numlist
