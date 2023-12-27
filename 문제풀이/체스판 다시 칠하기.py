# 백준 1018번 문제
# https://www.acmicpc.net/problem/1018


# --- 답안 1 (최적) ---
# 정답 체스판을 리스트로 직접 선언했음
# 정답 체스판 2가지 케이스를 둘다 구현할 필요 없고, 한가지 케이스로 구한 다음 나머지 케이스는 8*8에서 뺴면 된다는 점을 간파함
def solution():
    n, m = map(int, input().split())
    board = []
    for _ in range(n):
        string = input()
        board.append([ch for ch in string])
        
    chess_board = [
        ['W','B','W','B','W','B','W','B'],
        ['B','W','B','W','B','W','B','W'],
        ['W','B','W','B','W','B','W','B'],
        ['B','W','B','W','B','W','B','W'],
        ['W','B','W','B','W','B','W','B'],
        ['B','W','B','W','B','W','B','W'],
        ['W','B','W','B','W','B','W','B'],
        ['B','W','B','W','B','W','B','W'],
    ]
        
    answer = []
    for row in range(n - 8 + 1):
        for col in range(m - 8 + 1):
            new_board = [line[col:col+8] for line in board[row:row+8]]
            result = 0
            for new_row in range(8):
                for new_col in range(8):
                    if new_board[new_row][new_col] != chess_board[new_row][new_col]:
                        result += 1
            answer.append(min(result, 8*8 - result))
    return min(answer)

print(solution())


# --- 답안 2 ---
# DFS로 어렵게 접근한 답안. 정답 체스판 2가지 케이스 존재하는 예외처리는 안함
# def solution():
#     n, m = map(int, input().split())

#     board = []
#     for _ in range(n):
#         string = input()
#         board.append([ch for ch in string])
        
#     def dfs(row, col, adj_ch):
#         nonlocal new_board, visit, return_value

#         if row < 0 or row >= 8 or col < 0 or col >= 8 or visit[row][col]:
#             return -1

#         visit[row][col] = True
#         if new_board[row][col] == adj_ch:
#             new_board[row][col] = 'W' if adj_ch == 'B' else 'B'
#             return_value += 1

#         dfs(row+1, col, new_board[row][col]) # 아래
#         dfs(row, col+1, new_board[row][col]) # 오른쪽
    
#     answer = []
#     for row in range(n - 8 + 1):
#         for col in range(m - 8 + 1):
#             # new_board = board[row:row+8][col:col+8]  # 리스트에서는 이 문법이 안된다는 것을 유념하자!
#             new_board = [line[col:col+8] for line in board[row:row+8]]
#             visit = [[False] * 8 for _ in range(8)]
#             return_value = 0
#             dfs(0, 0, '')
#             answer.append(min(return_value, 8*8 - return_value))
            
#     return min(answer)
        
# print(solution())
