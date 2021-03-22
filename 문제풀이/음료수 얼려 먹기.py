
### 이것이 코딩 테스트다 with 파이썬 p.149 문제 ###
# DFS 이용


n, m = map(int, input().split())
graph = []
answer = 0  # 만들어진 덩어리 수
for _ in range(n):
    graph.append(list(map(int, input())))


def dfs(i, j):
    if 0 <= i <= n-1 and 0 <= j <= m-1:
        if graph[i][j] == 0:    # 미방문 노드인 경우
            graph[i][j] = 1     # 방문 처리

            # 인접 노드 재귀적으로 탐색
            dfs(i-1, j)
            dfs(i, j-1)
            dfs(i, j+1)
            dfs(i+1, j)
            return 1    # 덩어리 생성
    return 0    # 덩어리 생성 X

for row in range(n):
    for col in range(m):
        answer = answer + dfs(row, col) # 총 생성된 덩어리 수 카운팅

print("정답 : ", answer)
