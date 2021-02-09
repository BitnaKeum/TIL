
# 문제 : https://programmers.co.kr/learn/courses/30/lessons/42576


############### 1번째 답 #################
def solution(participant, completion):
    for name in completion:
        participant.remove(name)
    return participant[0]
    
# 정확도 테스트 통과, 효율성 테스트 비통과
###########################################


############### 2번째 답 #################
def solution(participant, completion):
    dict1 = {}
    dict2 = {}
    i=0
    for i in range(len(completion)):
        if participant[i] not in dict1.keys():
            dict1[participant[i]] = 1
        dict1[participant[i]] += 1
        
        if completion[i] not in dict2.keys():
            dict2[completion[i]] = 1
        dict2[completion[i]] += 1
            
    if participant[i+1] not in dict1.keys():
        dict1[participant[i+1]] = 1
    dict1[participant[i+1]] += 1
    
    for name in dict1.keys():
        if name not in dict2.keys() or dict1[name] != dict2[name]:
            return name
            
# 정확도 테스트 통과, 효율성 테스트 통과
###########################################


############### 3번째 답 #################
from collections import Counter

def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]
    
# 정확도 테스트 통과, 효율성 테스트 통과
###########################################
