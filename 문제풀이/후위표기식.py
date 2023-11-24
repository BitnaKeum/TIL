### 백준 1918번 후위표기식 문제
### 핵심: Stack 이용


# --- 답안 1 ---
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



# --- 답안 2 (최적) ---
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
