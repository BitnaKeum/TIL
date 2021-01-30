
##### 문제 : https://wikidocs.net/73 #####



com = int(input("number of computer : ")) # 컴퓨터 수
prog = input("program execution time : ").split()  # 프로그램 수행 시간
for i in range(len(prog)):
    prog[i] = int(prog[i])

prog.sort(reverse=True)    # prog를 내림차순으로 정렬

comp = {}
prog_sum = []
for i in range(com):    # 초기화
    comp[i] = []
    prog_sum.append(0)


for max_prog in prog:   # 가장 큰 값을 하나씩 꺼냄
    min_idx = prog_sum.index(min(prog_sum))     # 최소값의 인덱스

    comp[min_idx].append(max_prog)
    prog_sum[min_idx] += max_prog




# 결과 출력
for i in range(com):
    print("computer", i, ":", end=" ")

    for j in range(len(comp[i])):
        print(comp[i][j], end=" ")
    print()


