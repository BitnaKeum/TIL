# 프로그래머스 점 찍기 (https://school.programmers.co.kr/learn/courses/30/lessons/140107)
# 입력값의 범위가 크기 때문에 시간초과를 방지하기 위해 수학적 수식을 활용해야 하는 문제

def solution(k, d):
    answer = 0
    for x in range(0, d+1, k):
        y = (d**2 - x**2)**(1/2)
        answer += y // k + 1

    return answer
