# 책 이것이 코딩 테스트다 p.201 떡볶이 떡 만들기 문제

```
값의 갯수와 범위가 매우 크기 때문에 자동으로 이진 탐색을 떠올리는 것이 핵심.
```

def binary_search(arr, target, start, end):
    h_cands = []
    while start <= end:
        h = (start + end) // 2
        result = sum([num - h for num in arr if num > h]) # 잘린 떡의 길이 총합
        if result == target:
            return h
        elif result < target:
            end = h - 1
        else:
            h_cands.append(h)
            start = h + 1
    return max(h_cands) # 정확히 target만큼을 얻을 수 없는 경우
        

n, m = map(int, input().split())
lens = list(map(int, input().split()))
print(binary_search(lens, m, 0, lens[n-1]))
