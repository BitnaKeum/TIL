# 프로그래머스 멀쩡한 사각형 (https://school.programmers.co.kr/learn/courses/30/lessons/62048)
# 시간초과를 피하기 위해서 수학적인 접근과 패턴 파악이 필요
# 모범 답안 설명 영상 => https://www.youtube.com/watch?v=LZ94TH5L--8&t=162s

import math

# --- 모범 답안 ---
def solution(w,h):
    total_cnt = w * h
    gcd = math.gcd(w, h)
    remove_cnt_per_pattern = (w / gcd) + (h / gcd) - 1

    return total_cnt - gcd * remove_cnt_per_pattern


# --- 시간초과로 틀린 코드 ---
# def solution(w,h):
#     cnt = w * h
#     y_prev = h
#     for x in range(1, w+1):
#         y = -h/w*x + h
#         cnt -= math.ceil(y_prev) - int(y)
#         y_prev = y
#     return cnt
