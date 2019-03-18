import sys
sys.stdin = open('input.txt')

data = input()
binary = [0]*(len(data)*4)
for j in range(len(data)):
    for i in range(4):
        if int(data[j], 16) & (1 << (3-i)):
            binary[4*j+i] = 1

password = [[0,0,1,1,0,1],[0,1,0,0,1,1],[1,1,1,0,1,1],[1,1,0,0,0,1],[1,0,0,0,1,1],[1,1,0,1,1,1],[0,0,1,0,1,1],[1,1,1,1,0,1],[0,1,1,0,0,1],[1,0,1,1,1,1]]

k = 0
while k+6 < len(binary):
    for l in range(10):
        if binary[k:k+6] == password[l]:
            print(l)
            k += 6
            break
    else:
        k += 1