### 백준 1260번 문제 DFS와 BFS ###

from collections import deque

def dfs():
    visit = {}
    stack = [V]
    while stack:
        node = stack.pop()
        if node not in visit:
            visit[node] = True
            stack.extend(reversed(sorted(list(graph[node] - set(visit.keys())))))
    return ' '.join(str(key) for key in visit.keys())

def bfs():
    visit = {}
    queue = deque([V])
    while queue:
        node = queue.popleft()
        if node not in visit:
            visit[node] = True
            queue.extend(sorted(list(graph[node] - set(visit.keys()))))
    return ' '.join(str(key) for key in visit.keys())


N, M, V = map(int, input().split())

graph = [set() for _ in range(N + 1)]
for _ in range(M):
    num1, num2 = map(int, input().split())
    graph[num1].add(num2)
    graph[num2].add(num1)

print(dfs())
print(bfs())
