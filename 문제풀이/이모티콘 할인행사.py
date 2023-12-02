# 프로그래머스 2023 KAKAO BLIND RECRUITMENT 이모티콘 할인행사 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/150368?language=python3

""" 해결 방법
- users의 길이가 100 이하, emoticons의 길이가 7 이하 로 충분히 작음 => 모든 경우의 수를 탐색하는 완전탐색 알고리즘을 활용
- 모든 이모티콘 할인율에 대한 중복순열을 만들기 위해 itertools.product() 함수를 사용 (미사용시 DFS로 직접 구현해야함)
"""

# --- 작성한 코드가 나름 최적의 코드인듯하다 ---
import itertools

def solution(users, emoticons):
    emoticon_rate_cands = itertools.product([10, 20, 30, 40], repeat=len(emoticons))
    
    answer = [0, 0]
    for emoticon_rate in emoticon_rate_cands:  # (rate1, rate2, ...)  
        buy_price = [0] * len(users)    # user별 이모티콘 구매 누적 금액
        subscriber = 0  # 이모티콘 플러스 구독자 수
        
        for i in range(len(users)):
            for emoticon_price, emoticon_sale_rate in zip(emoticons, emoticon_rate):    # emoticon_price: 이모티콘 정가, emoticon_sale_rate: 이모티콘 할인 비율
                if emoticon_sale_rate >= users[i][0]:  # 구매
                    buy_price[i] += emoticon_price * (100-emoticon_sale_rate) / 100
                    
            if buy_price[i] >= users[i][1]: # 이모티콘 플러스 구독
                buy_price[i] = 0
                subscriber += 1
        
        if subscriber > answer[0]:
            answer[0] = subscriber
            answer[1] = sum(buy_price)
        elif subscriber == answer[0]:
            answer[1] = max(answer[1], sum(buy_price))

    return answer
