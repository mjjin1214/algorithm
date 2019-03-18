import sys
sys.stdin = open('input.txt')

data = input()
binary = [0]*(len(data)*4)
for j in range(len(data)):
    for i in range(4):
        if int(data[j], 16) & (1 << (3-i)):
            binary[4*j+i] = 1

t = 0
for k in range(len(binary)):
    t = t * 2 + int(binary[k])
    if (k+1) % 7 == 0:
        print(t, end=' ')
        t = 0
else:
    print(t)