# 프로그래머스 연습문제 디펜스 게임 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/142085

'''
값의 범위가 굉장히 커서 완전 탐색을 사용하는 것이 아닐걸 알았지만, 도저히 방법이 떠오르지 않아서 DFS로 접근했고 실패했음

무적권은 현재까지 거친 라운드 중에 적의 수가 가장 많은 상위 k개 경우에 사용해야함
매 라운드마다 해당 값(적의 수)을 무적권을 쓰려고 하는 k개 값과 대소 비교해야함
이를 위해서는 해당 값을 무적권 후보 리스트에 추가하고 가장 작은 값을 제거하면 됨
 => 매번 최소값을 구해야하네 => 'Heap을 사용해야겠구나'를 떠올리는 것이 핵심!!

Heap이나 Priority Queue 말고 다른 접근방법은 시간초과 때문에 없는 듯함.
'''


# --- 참고해서 작성한 답안 (최적) ---
import heapq

def solution(n, k, enemy):
    # n: 총 병사 수
    # k: 무적권 횟수
    # enemy[i]: 라운드별 적의 수
    # 남은 병사 수 < 현재 라운드의 적의 수 => 게임 종료
    # 무적권을 적절한 라운드에 사용하여 최대한 많은 라운드 진행하기
    # return: 막기 성공한 라운드 수
        
    heap = []
    
    for i in range(len(enemy)):
        heapq.heappush(heap, enemy[i])
        if len(heap) > k:
            min_value = heapq.heappop(heap)
            n -= min_value
            if n < 0:
                return i
    return len(enemy)
