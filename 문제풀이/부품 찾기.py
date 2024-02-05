# 책 이것이 코딩 테스트다 p.197 부품 찾기 문제

```
값의 갯수와 범위가 매우 크기 때문에, 단순 탐색이 아닌 효율적인 알고리즘을 사용하는 것이 핵심
그래서 이진 탐색 또는 해시 테이블로 구현하였음
```

# --- 답안1. 이진 탐색으로 구현 ---
def binary_search(arr, target, start, end):
    if start > end:
        return 'no'
    mid = (start + end) // 2
    if arr[mid] == target:
        return 'yes'
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid-1)
    else:
        return binary_search(arr, target, mid+1, end)

n = int(input())
n_arr = sorted(map(int, input().split()))
m = int(input())
m_arr = list(map(int, input().split()))
for target in m_arr:
    print(binary_search(n_arr, target, 0, n-1), end=" ")


# --- 답안2. 해시 테이블로 구현 ---
n = int(input())
n_arr = list(map(int, input().split()))
n_dict = {item: True for item in n_arr}
m = int(input())
m_arr = list(map(int, input().split()))

for item in m_arr:
    if item in n_dict:
        print("yes", end=" ")
    else:
        print("no", end=" ")
