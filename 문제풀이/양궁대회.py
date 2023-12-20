# 프로그래머스 2022 KAKAO BLIND RECRUITMENT 양궁대회 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/92342

# 처음에는 라이언이 이길 수 있는 케이스만 효율적으로 걸러내는 방식으로 접근하다보니 알고리즘이 굉장히 복잡해졌고 결국 제한시간내 구현 실패함
# n의 범위가 작고, 최대 경우의 수가 11H10으로 매우 크지 않기 때문에 완전 탐색으로 접근해야 했음! 그러니까 알고리즘이 꽤나 단순해짐
# 중복조합 라이브러리 기억해두자 (combinations_with_replacement)


from itertools import combinations_with_replacement

def solution(n, info):
    # n: 화살 개수 (1~10)
    # info: 어피치가 맞힌 과녁 점수의 개수(10점부터 0점까지 인덱스별로)
    # 목표: 어피치와 더 큰 점수 차이 -> 가장 낮은 점수를 더 많이 맞힌 경우
    # 라이언이 우승할 수 없는 경우는 return [-1]
    
    ryan_win_cases = []
    max_diff = 0
    cases = combinations_with_replacement(range(11), n)
    for case in cases:
        ryan_info = [case.count(score) for score in range(10, -1, -1)]
        
        sum_apeach, sum_ryan = 0, 0
        for idx in range(11):
            if info[idx] == ryan_info[idx] == 0:
                continue
                
            if info[idx] >= ryan_info[idx]:  # 어피치가 점수 획득
                sum_apeach += (10 - idx)
            else:                            # 라이언이 점수 획득
                sum_ryan += (10 - idx)
        
        diff = sum_ryan - sum_apeach
        if diff > 0 and diff == max_diff:
            ryan_win_cases.append(ryan_info)
        elif diff > max_diff:
            ryan_win_cases = [ryan_info]    # (점수 차, 라이언 점수 목록) 저장
            max_diff = diff
    if not ryan_win_cases:  # 라이언이 우승할 방법이 없는 경우
        return [-1]

    # 점수 차가 가장 큰 경우에서, 가장 낮은 점수를 많이 맞힌 경우 찾기
    # 이 부분은 좀 더 효율적으로 짤 수 있을것 같은데 아쉽...
    for idx in range(10, -1, -1):
        cnts = [win_case[idx] for win_case in ryan_win_cases]
        max_cnt = max(cnts)
        if max_cnt > 0:
            answer = []
            for i in range(len(cnts)):
                if cnts[i] == max_cnt:
                    answer.append(i)
            if len(answer) == 1:
                return ryan_win_cases[answer[0]]
