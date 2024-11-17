def solution(n):
    if(n==1):
        return [[1]]
    answer = [[0 for j in range(n)] for i in range(n)]
    x=0
    y=0
    dir = 'r' #진행 방향 결정
    for i in range(n*n):
        answer[x][y] = i+1
        if dir == 'r': # 오른쪽으로 가는 중이었으면
            y += 1 #오른쪽으로 한 칸
            if y == n-1 or answer[x][y+1] !=0: # 오른쪽으로 갈 수 없거나 이미 값이 들어가있으면
                dir = 'd' # 진행 방향 아래로 변경
                
            # 아래는 비슷하게 반복하면 됨
        elif dir == 'd':
            x += 1
            if x == n-1 or answer[x+1][y] !=0:
                dir = 'l'
        elif dir == 'l':
            y -= 1
            if y==0 or answer[x][y-1] != 0:
                   dir = 'u'
        elif dir == 'u':
            x -= 1
            if x==0 or answer[x-1][y] != 0:
                dir = 'r'
    return answer

