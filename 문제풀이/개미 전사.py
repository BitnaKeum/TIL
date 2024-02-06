# 책 이것이 코딩테스트다 p.220 개미 전사 문제

'''
배열을 순차적으로 지나면서 조건을 만족하는 값들의 누적 합을 계속 사용하기 때문에, 값을 반복적으로 사용한다고 보고 Dynamic Programming으로 풀 수 있음.
점화식 세우는 것이 조금 어려웠는데, 두가지 식을 세울 수 있다:
  1. d_i = max(d_{i-3}, d_{i-2}) + arr_i
  2. d_i = max(d_{i-1}, d_{i-2}+arr_i)
'''


# --- 답안1. 내 코드 (점화식 1) ---
n = int(input())
arr = list(map(int, input().split()))

d = [0] * n
d[0], d[1], d[2] = arr[0], arr[1], arr[0]+arr[2]
for i in range(3, n):
    d[i] = max(d[i-2], d[i-3]) + arr[i]

print(max(d[n-2], d[n-1]))


# --- 답안2. 책 코드 (점화식 2) ---
n = int(input())
arr = list(map(int, input().split()))

d = [0] * n
d[0] = arr[0]
d[1] = max(arr[0], arr[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + arr[i])

print(d[n-1])


# --- 답안3. 내 코드 (점화식으로 접근하지 않아서 간결하지 않음)
n = int(input())
arr = list(map(int, input().split()))

d = [0] * n
d[0], d[1] = arr[0], arr[1]
for i in range(n-2):
    # 두칸뛰기
    d[i+2] = max(d[i] + arr[i+2], d[i+2])
    # 세칸뛰기
    if i != n-3:
        d[i+3] = max(d[i] + arr[i+3], d[i+3])
    
print(max(d[n-2], d[n-1]))
