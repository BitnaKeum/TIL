# 책 이것이 코딩테스트다 p.217 1로 만들기 문제

'''
작은 값에 대한 연산이 반복되기 때문에 Dynamic Programming을 사용해야 함.
반복문을 사용하여 bottom-up 방식으로 구현하였음.
1을 빼는 경우를 가장 먼저 수행함으로써 배열의 값을 0이 아닌 다른 값으로 할당한다는 것을 떠올리기가 어려웠음.
'''

x = 26

d = [0] * (x+1)
for num in range(2, x+1):
    # 1 빼기
    d[num] = d[num-1] + 1 # 가장 연산 횟수 값이 크고, 무조건 수행되기 때문에 이 경우를 가장 먼저 수행
    
    if num % 5 == 0:
        d[num] = min(d[num], d[num//5] + 1)
    if num % 3 == 0:
        d[num] = min(d[num], d[num//3] + 1)
    if num % 2 == 0:
        d[num] = min(d[num], d[num//2] + 1)
    
print(d[x])
