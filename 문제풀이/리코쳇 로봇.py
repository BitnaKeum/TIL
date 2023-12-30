# 프로그래머스 연습문제 리코쳇 로봇 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/169199

'''
최소 이동 횟수를 구하는 문제이므로 BFS라고 생각했다가, 이미 방문한 노드를 재방문할 수 있다는걸 깨닫고 최단 경로를 구하는 것이 아니라고 생각함 => DFS로 접근했고 구현 실패.

BFS에서도 이미 방문한 노드를 재방문할 수 있다는 점을 새로 알게 됨. 이 경우, 각 노드에 도달한 거리를 따로 기록해줘야함. 그리고 해당 노드를 이미 방문한 적이 있을 때, 더 거리가 작은 값을 기록해주면 됨.

BFS/DFS 문제에서 dx = [-1, 1, 0, 0], dy = [0, 0, -1, 1]와 같이 작성하는 방식 익히기.
deque에서 append(), popleft() 사용. 
'''


# --- 답안 (최적) --- 
from collections import deque

def solution(board):
    for i in range(len(board)):
        st = board[i]
        if 'R' in st:
            r_row, r_col = i, st.index('R')
            break

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    dist = [[100000] * len(board[0]) for _ in range(len(board))]

    queue = deque()
    queue.append([r_row, r_col, 0])
    dist[r_row][r_col] = 0
    while queue:
        x, y, d = queue.popleft()
        for i in range(4):  # 상하좌우
            n_x, n_y = x, y
            is_move = False
            while 0<=n_x+dx[i]<len(board) and 0<=n_y+dy[i]<len(board[0]) and board[n_x+dx[i]][n_y+dy[i]] != 'D':    # 한번 이동
                n_x, n_y = n_x+dx[i], n_y+dy[i]
                is_move = True
            if is_move:
                if board[n_x][n_y] == 'G':
                    return d+1
                if d+1 < dist[n_x][n_y]:
                    dist[n_x][n_y] = d+1
                    queue.append([n_x, n_y, d+1])
    return -1
