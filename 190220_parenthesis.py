import sys

sys.stdin = open('input.txt', 'r')

data = input()

stack = [0]*10  # 시험시 10000
top = -1

info = [0] * 128  # char 1byte ASCII code 7bit

for j, k in zip(')}]>', '({[<'):
    info[ord(j)] = k

for i in data:
    if i == '(' or i == '{' or i == '[' or i == '<':
        top += 1
        stack[top] = i
        print(stack)
    elif i == ')' or i == '}' or i == ']' or i == '>':
        if info[ord(i)] == stack[top]:
            stack[top] = 0
            top -= 1
            print(stack)
        else:
            print('에러')
            break
    else:
        continue
else:
    if top != -1:
        print('에러')
    else:
        print('황준우')

# while top != -1:
#     print(stack[top])
#     top -= 1
