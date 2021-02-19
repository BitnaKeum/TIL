
# 주어진 문자열이 팰린드롬(뒤집어도 같은 문자열)인지 판별한다. 단, 대소문자를 구분하지 않고, 영문자와 숫자만을 대상으로 한다.

########### 1번째 답 ###############
# 리스트 사용, 비효율적인 코드

def func(st):
    p_s = []
    p_s_rev = []
    for s in st:
        if s.isalnum():
            p_s.append(s.lower())
    for idx in range(len(p_s)-1, -1, -1):
        p_s_rev.append(p_s[idx])
    print(p_s == p_s_rev)


st = "A man, a plan, a canal: Panama"
func(st)

#####################################


########### 2번째 답 ###############
# pop()을 더 빠르게 사용할 수 있는 deque 이용

import collections

def func(st: str):
    deq = collections.deque()

    for ch in st:
        if ch.isalnum():
            deq.append(ch.lower())

    while len(deq) > 1:
        if deq.popleft() != deq.pop():
            return False
    return True


st = "A man, a plan, a canal: Panama"
print(func(st))

#####################################


########### 3번째 답 ###############
# 정규식과 슬라이싱 사용

import re

def func(st: str) -> bool:
    st = st.lower() # 소문자 변환
    st = re.sub('[^a-z0-9]', '', st)    # 영문자, 숫자만 남김
    return st == st[::-1]


st = "A man, a plan, a canal: Panama"
print(func(st))

#####################################
