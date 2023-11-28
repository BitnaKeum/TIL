# 프로그래머스 2023 KAKAO BLIND RECRUITMENT 개인정보 수집 유효기간 문제 (https://school.programmers.co.kr/learn/courses/30/lessons/150370)


# --- 나의 답안 ---
# 년, 월, 일 형식을 유지하려다보니 코드가 조금 복잡해짐
def solution(today, terms, privacies):
    # today: YYYY.MM.DD
    # terms: 약관종류(A~Z) 유효기간(1~100)
    # privacies: 약관수집일자 약관종류
    
    answer = []
    
    today = today.replace('.', '')
    valid_month = {term[0]: int(term[2:]) for term in terms}
    for num, privacy in enumerate(privacies):
        start_date, type_name = privacy.split()
        year, month, day = map(int, start_date.split('.'))
        
        term_month = valid_month[type_name]
        year = year + term_month // 12
        month = month + term_month % 12
        if month > 12:
            month = month - 12
            year = year + 1

        # end_date는 만료일 + 1일이므로 today와 같거나 작을 때 파기해야함
        end_date = str(year)
        end_date += str(month) if month >= 10 else '0' + str(month)
        end_date += str(day) if day >= 10 else '0' + str(day)
        if end_date <= today:
            answer.append(num+1)

    return answer


# --- 모범 답안 ---
# 년, 월, 일 을 모두 일 로 변환해서 훨씬 깔끔한 코드
def solution(today, terms, privacies):
    answer = []
  
    term_dict = {term[0]: int(term[2:]) * 28 for term in terms}
  
    year, month, day = map(int, today.split('.'))
    total_today = 28 * 12 * year + 28 * month + day

    for p in range(len(privacies)):
        pret = privacies[p].split(' ')
        year, month, day = map(int, pret[0].split('.'))
        total = 28 * 12 * year + 28 * month + day

        if term_dict[pret[1]] + total <= total_today:
            answer.append(p + 1)

    return answer
