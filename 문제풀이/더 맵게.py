# 프로그래머스 Lv2 더 맵게
# 매번 정렬이 되어야 하고 pop을 사용해야하기 때문에 Heap을 떠올리는 것이 핵심!

import heapq

def solution(scoville, K):
    cnt = 0 

    heap_list = []
    for val in scoville:
        heapq.heappush(heap_list, val)

    while True:
        if heap_list[0] >= K:
            return cnt
        elif len(heap_list) == 1:
            return -1

        low1 = heapq.heappop(heap_list)
        low2 = heapq.heappop(heap_list)
        new_score = low1 + (low2 * 2)
        heapq.heappush(heap_list, new_score)
        cnt += 1
