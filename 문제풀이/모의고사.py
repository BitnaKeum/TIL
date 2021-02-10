
# 문제 : https://programmers.co.kr/learn/courses/30/lessons/42840



################# 1번째 답 ########################   

def solution(answers):
    num = len(answers)  # 문제 수
    
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]

    answer1 = [p1[i%5] for i in range(num)]
    answer2 = [p2[i%8] for i in range(num)]
    answer3 = [p3[i%10] for i in range(num)]

    answer_cnt = [0, 0, 0]
    for i, answer in enumerate(answers):
        if answer1[i] == answer:
            answer_cnt[0] += 1
        if answer2[i] == answer:
            answer_cnt[1] += 1
        if answer3[i] == answer:
            answer_cnt[2] += 1
            
    max_cnt = max(answer_cnt)
    winner = []
    for i, cnt in enumerate(answer_cnt):
        if cnt == max_cnt:
            winner.append(i+1)
            
    return winner
    
###################################################
    
    
################# 2번째 답 ########################   
    
# 완전탐색은 아니지만 조금 더 간결한 코드
def solution(answers):
    num = len(answers)  # 문제 수
    
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]

    answer1 = [p1[i%5] for i in range(num) if p1[i%5] == answers[i]]
    answer2 = [p2[i%8] for i in range(num) if p2[i%8] == answers[i]]
    answer3 = [p3[i%10] for i in range(num) if p3[i%10] == answers[i]]
    
    answer_cnt = [len(answer1), len(answer2), len(answer3)]
    max_cnt = max(answer_cnt)
    winner = []
    for i, cnt in enumerate(answer_cnt):
        if cnt == max_cnt:
            winner.append(i+1)
            
    return answer
    
###################################################
