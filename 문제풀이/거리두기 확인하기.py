# 프로그래머스 거리두기 확인하기 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/81302#fn1

from itertools import combinations

def find_positions(place):
    positions = []
    for row in range(len(place)):
        s = place[row]
        for col in range(len(s)):
            if s[col] == 'P':
                positions.append((row, col))
    return positions

def check_place(place):
    positions = find_positions(place)
    combs = list(combinations(positions, 2))
    for (pos1, pos2) in combs:
        dist = abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
        if dist <= 2:   # 파티션 있는지 확인해야함
            # 행이 같거나, 열이 같거나, 대각선
            if pos1[0] == pos2[0] and place[pos1[0]][pos1[1]+1] != 'X':
                return 0
            elif pos1[1] == pos2[1] and place[pos1[0]+1][pos1[1]] != 'X':
                return 0
            elif pos1[1] < pos2[1] and not (place[pos1[0]][pos1[1]+1] == 'X' and place[pos2[0]][pos2[1]-1] == 'X'):
                return 0
            elif pos1[1] > pos2[1] and not (place[pos1[0]][pos1[1]-1] == 'X' and place[pos2[0]][pos2[1]+1] == 'X'):
                return 0
    return 1

def solution(places):
    return [check_place(place) for place in places]
