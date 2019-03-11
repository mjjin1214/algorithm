import sys
sys.stdin = open('input.txt', 'r')

data = list(map(int, input().split()))
length = len(data)
matrix = [data[0]]+[0]*(length-1)
for i in range(1, length):
    temp = data[i]
    while i > 0:
        if temp < matrix[i - 1]:
            matrix[i] = matrix[i-1]
            i -= 1
            if i == 0:
                matrix[i] = temp
        else:
            matrix[i] = temp
            break

print(matrix)
