### 백준 1918번 후위표기식 문제 (https://www.acmicpc.net/problem/1918)
### 핵심: Stack 이용



# --- 답안 1 (최적) ---
import sys

eq = input()
stack = []
result = ''
priority_map = {'+': 0, '-': 0, '*': 1, '/': 1, '(': -1}

for ch in eq:
    if ch.isalpha():
        result += ch
    elif ch == '(':
        stack.append(ch)
    elif ch == ')':
        while stack and stack[-1] != '(':
            result += stack.pop()
        else:
            stack.pop()
    else: # '+', '-', '*', '/'
        while stack and priority_map[stack[-1]] >= priority_map[ch]:
            result += stack.pop()
        stack.append(ch)
while stack:
    result += stack.pop()

print(result)


# --- 답안 2 ---
# eq = input()

# stack = []
# result = ''

# for ch in eq:
#     if ch >= 'A' and ch <= 'Z':
#         result += ch
#     elif ch == '+' or ch == '-':
#         while stack and stack[-1] != '(':
#             result += stack.pop()
#         stack.append(ch)
#     elif ch == '*' or ch == '/':
#         while stack and (stack[-1] == '*' or stack[-1] == '/'):
#             result += stack.pop()
#         stack.append(ch)
#     elif ch == '(':
#         stack.append(ch)
#     elif ch == ')':
#         while stack[-1] != '(':
#             result += stack.pop()
#         stack.pop()
# while stack:
#     result += stack.pop()
        
# print(result)



# --- Stack 안쓰고 한 시도 (틀림) --- 
# def transform(eq, memory, cnt):
#     while len(eq) > 1:
#         if '(' in eq:
#             start_idx = eq.index('(')
#             end_idx = eq.index(')')
#             target = eq[start_idx+1:end_idx]
#             if len(target) == 3:
#                 new_ch = chr(97+cnt)
#                 memory[new_ch] = target[0] + target[2] + target[1]
#                 eq = eq[:start_idx] + new_ch + eq[end_idx+1:]
#                 cnt += 1
#             else:
# #                 eq = eq.replace('(', '').replace(')', '')
#                 new_ch, memory, cnt = transform(target, memory, cnt)
#                 eq = eq[:start_idx] + new_ch + eq[end_idx+1:]
#         else:
#             if '*' in eq:
#                 start_idx = eq.index('*')
#             elif '/' in eq:
#                 start_idx = eq.index('/')
#             elif '+' in eq:
#                 start_idx = eq.index('+')
#             elif '-' in eq:
#                 start_idx = eq.index('-')
#             eq = eq[:start_idx-1] + '(' + eq[start_idx-1:start_idx+2] + ')' + eq[start_idx+2:]   
#     return eq, memory, cnt

# eq = input()
# memory = {}
# cnt = 0
# eq, memory, cnt = transform(eq, memory, cnt)

# for ch in list(memory.keys()):
#     eq = eq.replace(ch, memory[ch])
# while eq != eq.upper():
#     for ch in list(memory.keys()):
#         eq = eq.replace(ch, memory[ch])
    
# print(eq)
