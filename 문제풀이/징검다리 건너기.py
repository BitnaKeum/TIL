# 프로그래머스 2019 카카오 개발자 겨울 인턴십 징검다리 건너기 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/64062?language=python3#

'''
리스트 크기와 값의 범위가 크기 때문에 이진 탐색을 사용해야 함. 그런데 문제를 보고 이진 탐색을 어떻게 적용해야할지 떠올리는게 쉽지 않았음.
stones 배열에 이진 탐색을 적용하려고 했으나 도저히 방법이 보이지 않았음.
-> 니니즈 친구들의 수에 이진 탐색을 적용하는 것이 핵심.
   stones 배열의 각 값이 건널 수 있는 친구들의 수를 의미하므로, max(stones)를 end로 설정해야 함.
   리스트에서 특정 값이 몇번 연속되는지 구하는 새로운 방법을 터득함
'''


# --- 답안1. 최적의 코드 (정확도 100% 통과, 효율성 100% 통과) ---
def solution(stones, k):
    answer = 0
    start, end = 1, max(stones)
    while start <= end:
        mid = (start + end) // 2
        
        skip_cnt = 0
        for s in stones:
            if s < mid:
                skip_cnt += 1
                if skip_cnt >= k: # 사람 줄여야함
                    end = mid - 1
                    break
            else:
                skip_cnt = 0
        if skip_cnt < k: # 사람 늘려도됨
            answer = max(answer, mid)
            start = mid + 1

    return answer


# --- 답안2. 정확도 100% 통과, 효율성 50% 통과 ---
def solution(stones, k):
    answer = 0
    start, end = 1, max(stones)
    while start <= end:
        mid = (start + end) // 2
            
        res = "".join(['X' if s < mid else 'O' for s in stones])
        if 'X' * k in res:  # 사람 줄여야함
            end = mid - 1
        else:   # 사람 늘려도됨
            answer = max(answer, mid)
            start = mid + 1

    return answer


# --- 답안3. 정확도 100% 통과, 효율성 0% 통과 ---
def solution(stones, k):
    answer = 0
    while True:
        s = "_" + "_".join(map(str, stones))
        if '_0' * k in s:
            return answer
        answer += 1
        stones = list(map(lambda x: x-1 if x > 0 else 0, stones))

    return answer
