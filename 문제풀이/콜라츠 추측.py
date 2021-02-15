
# 문제 : https://programmers.co.kr/learn/courses/30/lessons/12943


def solution(num):
    if num == 1: return 0

    if num % 2 == 0:  # 짝수
        res = solution(num/2)
    else:   # 홀수
        res = solution(num*3 + 1)

    if res >= 500 or res == -1:  # 전체 수행 횟수 >= 500인 경우
        return -1
    else:    # 전체 수행 횟수 < 500인 경우
        return 1 + res
