### 프로그래머스 가장 큰 수
### 테스트 1~6 미통과 ㅠ

# Ver1
def solution(numbers):
    answer = ''
    if set(numbers) == {0}: # 모두 0
        return '0'
    numbers = [str(num) for num in numbers]
    numbers.sort(reverse=True)
        
    for crt_idx in range(0, len(numbers)-1):
        crt_num = numbers[crt_idx]
        for check_idx in range(crt_idx + 1, len(numbers)):
            check_num = numbers[check_idx]
            if check_num[0] != crt_num[0]:
                break
            if crt_num + check_num < check_num + crt_num:
                numbers.remove(check_num)
                numbers.insert(crt_idx, check_num)
                crt_idx += 1
    answer += ''.join(numbers)
                    
    return answer
  
  
  
  
# Ver2
#   answer = ''
#     if set(numbers) == {0}: # 모두 0
#         return '0'
#     numbers = [str(num) for num in numbers]
#     numbers.sort(reverse=True)

    
#     for start_num in range(9, -1, -1):
#         # start_num으로 시작하는 값들을 모은 배열
#         num_array = []
#         while len(numbers) > 0:
#             if numbers[0][0] == str(start_num):
#                 num_array.append(numbers[0])
#                 numbers.remove(numbers[0])
#             else: 
#                 break

#         for num in num_array:
#             if len(num) == 1:
#                 answer += num
#                 continue
                
#             idx = 1
#             while True:
#                 if num[idx] > num[0]:  # idx 자리가 첫째 자리보다 클 때
#                     if idx != len(num)-1:
#                         idx += 1
#                     answer += num    
#                     break
#                 else:
#                     if num[:idx] in num_array: # 한 자리 적은 값 넣기
#                         answer += num[:idx]
#                         num_array.remove(num[:idx])
#                         if idx == len(num)-1:
#                             answer += num
#                             break
#                         idx += 1
#                     else:
#                         if idx == len(num)-1:
#                             answer += num
#                             break

#                         idx += 1
                        
#     return answer

# print(solution([0, 0, 0]))
# print(solution([15, 151]))
