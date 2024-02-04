# 프로그래머스 과제 진행하기 Lv.2 문제 (정답률 37%)
# https://school.programmers.co.kr/learn/courses/30/lessons/176962

'''
문제에 나와있는 조건을 하나하나 다 구현하여서 코드가 불필요하게 길어짐.
start와 playtime을 따로 처리하지말고 끝나는 시간으로 합쳐서 처리했으면 알고리즘이 더 간단해졌을 것.
'''

# --- 답안1: 내 코드 ---
def solution(plans): 
    answer = []
    undone_stack = []

    # 시작 시각을 분 단위로 변환하고 시작 시간 순으로 정렬
    plans = sorted(map(lambda x: [x[0], int(x[1][:2]) * 60 + int(x[1][3:]), int(x[2])], plans), key=lambda x: -x[1])

    last_idx = len(plans) - 1
    for idx, (name, start, playtime) in enumerate(plans):
        if idx < last_idx:
            cur_end = start + playtime
            next_start = plans[idx+1][1]
            if cur_end < next_start: # 지금 end_time < 다음 start_time
                answer.append(name)
                while undone_stack:
                    name, playtime = undone_stack.pop()
                    possible_time = next_start - cur_end # 남은 시간
                    if possible_time > playtime:
                        answer.append(name)
                        cur_end += playtime
                    elif possible_time == playtime:
                        answer.append(name)
                        break
                    else:
                        playtime -= possible_time
                        undone_stack.append([name, playtime])
                        break
            elif cur_end == next_start: # 지금 end_time == 다음 start_time
                answer.append(name)
            else:   # 지금 end_time > 다음 start_time
                playtime -= (next_start - start)
                undone_stack.append([name, playtime])

        else:  # idx == final_idx
            answer.append(name)
            while undone_stack:
                answer.append(undone_stack.pop()[0])

    return answer


# --- 답안2: 최적의 코드 ---
def solution(plans):
    plans = sorted(map(lambda x: [x[0], int(x[1][:2]) * 60 + int(x[1][3:]), int(x[2])], plans), key=lambda x: -x[1])

    lst = []
    while plans:
        x = plans.pop()
        for i, v in enumerate(lst):
            if v[0] > x[1]:
                lst[i][0] += x[2]
        lst.append([x[1] + x[2], x[0]])
    lst.sort()

    return list(map(lambda x: x[1], lst))
