
########### '이것이 코딩 테스트다 with 파이썬' p.118 문제 ##############



dir = [0, 1, 2, 3] # 방향 (북, 동, 남, 서)
dx = [0, 1, 0, -1]  # 방향에 따른 좌우 이동
dy = [-1, 0, 1, 0]  # 방향에 따른 상하 이동

answer = 0  # 방문한 칸의 수 카운팅
n, m = map(int, input().split())
row, col, cur_dir = map(int, input().split()) # 현재 행, 현재 열, 현재 방향

# 게임 맵 입력받음 (0: 육지, 1; 바다)
game_map = []
for i in range(n):
  game_map.append(list(map(int, input().split())))


# 시뮬레이션 시작
while True:
  temp_row, temp_col = row, col

  if game_map[row-1][col] and game_map[row][col-1] and game_map[row+1][col] and game_map[row][col+1]: # 네 방향 모두 가본칸/바다
    temp_row, temp_col = row + dy[cur_dir], col + dx[cur_dir]
    
    if game_map[temp_row][temp_col] == 1: # 현재 방향의 뒤쪽 칸이 바다인 경우 멈춤
      break
    else:
      row, col = temp_row, temp_col
      continue


  cur_dir = dir[cur_dir - 1]  # 왼쪽으로 회전

  temp_row, temp_col = row - dy[cur_dir], col - dx[cur_dir]

  if game_map[temp_row][temp_col] == 0:  # 가보지 않은 육지
    row, col = temp_row, temp_col
    game_map[row][col] = 2
    answer = answer + 1

print(answer)
