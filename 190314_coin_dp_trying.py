change = int(input())
coin = [1, 1]

count = [0]+[0]*change

for i in range(1, change+1):
    if i % 10 == 0:
        count[i] = coin[1]
        coin[1] += 1
    elif i % 5 == 0:
        count[i] = coin[0]
        coin[0] += 1
    else:
        count[i] = count[i-1]+1

print(count[change])