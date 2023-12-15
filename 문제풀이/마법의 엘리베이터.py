# 프로그래머스 마법의 엘리베이터 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/148653#

def solution(storey):
    result = 0

    while storey > 0:
        num = storey % 10
        if num > 5: # 6 ~ 9
            result += (10 - num)
            storey = storey // 10 + 1
        elif num < 5: # 0 ~ 4
            result += num
            storey = storey // 10
        else:        # 5
            if (storey // 10) % 10 >= 5:
                storey = storey // 10 + 1
            else:
                storey = storey // 10
            result += num

    return result
