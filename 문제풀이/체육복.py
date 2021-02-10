
# 문제 : https://programmers.co.kr/learn/courses/30/lessons/42862


def solution(n, lost, reserve):
    answer = n - len(lost)  # 전체 학생 수 - 체육복 잃어버린 학생 수 (체육복을 빌렸을 때마다 증가시킬 것임)
    
    for l in lost:
        # 자신의 여벌 체육복이 있는 경우 우선순위
        if l in reserve:  
            reserve.remove(l)
            
        # 앞번호 학생이 여벌 체육복이 있는 경우 (앞번호 학생이 lost와 reserve에 동시 존재할 수는 없음)
        elif l-1 in reserve: 
            reserve.remove(l-1)
            
        # 뒷번호 학생이 여벌 체육복이 있는 경우 (뒷번호 학생은 lost와 reserve에 동시 존재할 수 있으므로 확인 필요)
        elif l+1 in reserve and l+1 not in lost:   
            reserve.remove(l+1)
            
        else:
            continue
            
        answer += 1   # 체육복을 빌렸으므로 체육복 있는 학생 수 1 증가
    
    return answer
