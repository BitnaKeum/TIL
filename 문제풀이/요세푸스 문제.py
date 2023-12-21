# 백준 1158번 요세푸스 문제 (실버4)
# https://www.acmicpc.net/problem/1158

n, k = map(int, input().split())

p = list(range(1, n+1))
answer = []
idx = 0
while p:
    idx += (k-1)
    idx = idx % len(p)
    answer.append(str(p[idx]))
    del p[idx]
print('<' + ', '.join(answer) + '>')
