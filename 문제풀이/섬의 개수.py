# 책 파이썬 알고리즘 인터뷰 p.331
# https://leetcode.com/problems/number-of-islands/
# DFS 이용. 음료수 얼려먹기 문제랑 동일

def dfs(row, col):
    if row < 0 or row >= 4 or col < 0 or col >= 5:
        return
    if grid_map[row][col] == 0:
        return

    global grid_map
    grid_map[row][col] = 0
    
    dfs(row-1, col)
    dfs(row+1, col)
    dfs(row, col-1)
    dfs(row, col+1)
    
    
answer = 0
grid_map = []
for _ in range(4):
    grid_map.append(list(map(int, input())))

for i in range(4):
    for j in range(5):
        if grid_map[i][j] == 1:
            dfs(i, j)
            answer += 1

print(answer)
