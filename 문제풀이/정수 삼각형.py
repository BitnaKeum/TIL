# 프로그래머스 정수 삼각형 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/43105

'''
처음에는 최댓값을 갖는 경로를 찾기 위해 모든 경로를 거쳐야한다고 생각해서 DFS로 구현함. 
=> 현재까지의 합계를 의미하는 sum 파라미터를 사용하여 나름 효율적일 것이라 생각했으나 시간 초과 테스트케이스에서 불통과.
경로를 찾을 필요가 없으므로 DFS 사용 X.
한번 계산된 합계를 저장해놓고 재사용하는 Dynamic Programming을 사용하는 것이 핵심.
'''

# --- 최적의 답안 (DP 사용) ---
def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(i+1):
            if j == 0:   # 첫번째 열
                triangle[i][j] += triangle[i-1][j]
            elif j == i: # 마지막 열
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    return max(triangle[-1])


# --- 비효율적인 답안 (DFS 사용) ---
# def solution(triangle):
#     global answer
#     answer = 0
    
#     def dfs(row_idx, col_idx, sum):
#         nonlocal triangle
#         sum += triangle[row_idx][col_idx]
#         if row_idx == len(triangle) - 1: # 마지막 행
#             global answer
#             if sum > answer:
#                 answer = sum
#             return
#         dfs(row_idx+1, col_idx, sum)
#         dfs(row_idx+1, col_idx+1, sum)
    
#     dfs(0, 0, 0)
#     return answer
