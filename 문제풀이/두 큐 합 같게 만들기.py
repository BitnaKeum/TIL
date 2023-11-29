# 프로그래머스 2022 KAKAO TECH INTERNSHIP 두 큐 합 같게 만들기 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/118667

"""
메모: 
좀 더 심화적이고 복잡하게 푸는 문제일 줄 알았는데 내가 취한 접근법이 옳은 방향이었음.
문제에 명시된 '이 문제에서는 큐를 배열로 표현하며' 문구 때문에 deque가 아닌 list로 구현하는 것을 조건으로 인지했는데 아니었음.
시간 초과를 해결하는 것이 이 문제의 핵심 포인트
  1. list 대신 deque 이용
  2. 각 queue의 원소 합을 iteration마다 sum()으로 구하지 말고 처음 구해놓은 다음에 더해지는/빼지는 값만 업데이트하기
  3. 두 queue의 값이 계속해서 서로 swap되면서 무한루프 도는 케이스 존재 => 초기 queue의 크기를 가지고 최대 반복 횟수 지정하기 (내가 이 부분을 생각 못했음)
"""


from collections import deque

def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    
    cnt_limit = len(queue1) * 4
    
    queue1_sum, queue2_sum = sum(queue1), sum(queue2)
    total = queue1_sum + queue2_sum
    if total % 2 != 0:
        return -1
    target_sum = total / 2
    
    cnt = 0
    while True:
        if queue1_sum == target_sum:
            return cnt
        elif queue1_sum < queue2_sum:
            num = queue2.popleft()
            queue1.append(num)
            queue1_sum += num
            queue2_sum -= num
            cnt += 1
        else:
            num = queue1.popleft()
            queue2.append(num)
            queue1_sum -= num
            queue2_sum += num
            cnt += 1

        if not queue1 or not queue2 or cnt > cnt_limit:
            return -1
