def solution(board):
    answer = 0
    n = len(board)
    # 탐색 방향 정하기
    dx = [-1,1,0,0,-1,-1,1,1]
    dy = [0,0,-1,1,-1,1,-1,1]
    # 지뢰가 설치된 좌표 구하기
    bomb = []
    for i in range (n):
        for j in range(n):
            if board[i][j]==1:
                bomb.append((i,j))
    #지뢰의 상하좌우대각선 값들을 모두 1로 바꾸기     
    for x,y in bomb:
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            #끝부분에 있는지 체크하는 거
            if 0<=nx <n and 0<=ny<n:
                board[nx][ny] = 1
    #1이 아닌 값들 세기
    count = 0
    for x in range(n):
        for y in range(n):
            if board[x][y]==0:
                count +=1
        
    return count