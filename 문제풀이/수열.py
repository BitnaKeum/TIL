# 백준 2491번 수열 (https://www.acmicpc.net/problem/2491)
# 구현 / dynamic programming 유형


# --- 효율적인 코드 ---
n = int(input())
seq = list(map(int, input().split()))

max_len = ascend_len = descend_len = 1
prev = seq[0]
for i in range(1, n):
    cur = seq[i]
    if prev < cur:    # ascend
        max_len = descend_len if descend_len > max_len else max_len
        ascend_len += 1
        descend_len = 1
    elif prev > cur:    # descend
        max_len = ascend_len if ascend_len > max_len else max_len
        ascend_len = 1
        descend_len += 1
    else:    # same
        ascend_len += 1
        descend_len += 1
    prev = cur
    
print(max(max_len, ascend_len, descend_len))



# --- 참신했던 코드 ---
def func(s, e, sign, max_cnt):
    cnt = 1
    for i in range(s, e, sign):
        if arr[i] <= arr[i + sign]:
            cnt += 1
        else:
            if max_cnt < cnt:
                max_cnt = cnt
            cnt = 1
    if max_cnt < cnt:
        max_cnt = cnt
    return max_cnt

N = int(input())
arr = list(map(int, input().split()))
max_cnt = 1
max_cnt = func(0, N-1, 1, max_cnt)
max_cnt = func(N-1, 0, -1, max_cnt)
print(max_cnt)



# --- 비효율적인 코드 ---
# 처음에 먼저 충분히 생각하지 않고 일단 이렇게 해보자하고 구현하다보니 점점 비효율적이어짐
# n = int(input())
# seq = list(map(int, input().split()))

# if n == 1:
#     print(1)
# else:
#     is_ascend, is_descend = False, False
#     if seq[0] <= seq[1]:
#         is_ascend = True
#     if seq[0] >= seq[1]:
#         is_descend = True
#     max_length, length, same_length = 2, 2, 0
    
#     prev = seq[1]
#     for cur in seq[2:]:
#         if cur > prev:    # ascend
#             if is_ascend:
#                 length += 1
#                 is_descend = False
#             elif is_descend:
#                 max_length = length if length > max_length else max_length
#                 length = same_length + 2
#                 is_ascend = True
#                 is_descend = False
#             same_length = 0
#         elif cur < prev:    # descend
#             if is_ascend:
#                 max_length = length if length > max_length else max_length
#                 length = same_length + 2
#                 is_ascend = False
#                 is_descend = True
#             elif is_descend:
#                 length += 1
#                 is_ascend = False
#             same_length = 0
#         else: # same
#             length += 1
#             if is_ascend:
#                 is_descend = False
#             elif is_descend:
#                 is_ascend = False
#             same_length += 1
#         prev = cur
    
#     max_length = length if length > max_length else max_length
#     print(max_length)
