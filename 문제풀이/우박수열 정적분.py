# 프로그래머스 Lv.2 40% 우박수열 정적분 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/134239

# 문제는 잘 이해했다면 어렵지 않은데, 정답률이 생각보다 낮은 이유는 사람들이 수학에 덜컥 겁먹어서가 않을까..

def solution(k, ranges):
    answer = []
    
    numbers = [k]
    while k != 1:
        k = k / 2 if k % 2 == 0 else k * 3 + 1
        numbers.append(k)

    areas = []
    n = len(numbers) - 1
    for x in range(n):
        areas.append((numbers[x] + numbers[x+1]) / 2)
    
    for a, b in ranges:
        b = n + b if b <= 0 else b
        if a > b:
            answer.append(-1)
        elif a == b:
            answer.append(0)
        else:
            answer.append(sum(areas[a:b]))

    return answer
