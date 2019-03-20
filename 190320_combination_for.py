import sys
sys.stdin = open('input2.txt')

for i in range(1, 4):
    for j in range(i+1, 4):
        if i == j:
            continue
        print(i, j)