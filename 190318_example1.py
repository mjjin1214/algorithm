import sys
sys.stdin = open('input.txt')

data = list(map(int, list(input())))
temp = 0
for i in range(len(data)):
    temp |= (data[i] << 6-(i%7))
    if (i+1) % 7 == 0:
        print(temp)
        temp = 0

tempp = ''
for j in range(len(data)):
    tempp += str(data[j])
    if (j+1) % 7 == 0:
        print(int('0b'+tempp, 2))
        tempp = ''

t = 0
for k in range(len(data)):
    t = t * 2 + int(data[k])
    if (k+1) % 7 == 0:
        print(t, end=' ')
        t = 0
