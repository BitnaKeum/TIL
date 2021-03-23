
### 이것이 코딩테스트다 with 파이썬 p.154? 문제 ###
# DFS 이용

def dfs(row, col, cnt):
    if 0 <= row <= n-1 and 0 <= col <= m-1:

        if miro[row][col] == 1: # 괴물이 없는 칸
            miro[row][col] = cnt + 1    # 들른 칸의 수를 증가시키며 저장
            cnt = cnt + 1

            if row == n - 1 and col == m - 1:  # 출구에 도착하면 재귀함수 탈출
                pass
            else:
                dfs(row+1, col, cnt)
                dfs(row, col+1, cnt)
                dfs(row-1, col, cnt)
                dfs(row, col-1, cnt)
                
                
                
n, m = map(int, input().split())
miro = []
for _ in range(n):
    miro.append(list(map(int, input())))
cnt = 0     # 방문한 칸의 수

dfs(0, 0, cnt)
print("answer : ", miro[n-1][m-1])
