# 프로그래머스 연습문제 바탕화면 정리 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/161990


# --- 답안1. 더 깔끔한 코드 ---
def solution(wallpaper):
    x, y = [], []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                x.append(i)
                y.append(j)
                
    return [min(x), min(y), max(x)+1, max(y)+1]


# --- 답안2. 덜 깔끔하지만 조금 더 효율적인 코드 (내 답안) ---
def solution(wallpaper):
    luy, lux = 100, 100
    rdy, rdx = -1, -1
    
    for y, s in enumerate(wallpaper):
        x = s.find('#')
        if x != -1:
            if x < luy:
                luy = x
            x = s.rfind('#')
            if x+1 > rdy:
                rdy = x+1
            if y < lux:
                lux = y
            if y+1 > rdx:
                rdx = y+1
                
    return [lux, luy, rdx, rdy]
