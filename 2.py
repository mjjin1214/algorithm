def prime(x):
    if x < 2:
        return False
    j = 2
    while j*j < x+1:
        if not x % j:
            return False
        j += 1
    else:
        return True


isnotprime = [0]*123456
prime = [0]*123456
primeidx = -1
isnotprime[0] = isnotprime[1] = True

for now in range(2, 123456):
    if isnotprime[now] == False:
        primeidx += 1
        prime[primeidx] = now
        for i in range(now*now, 123456, now):
            isnotprime[i] = True
print(prime)
while True:
    n = int(input())
    if n == 0:
        break
    count = 0
    for j in prime:
        if n < j <= 2*n:
            count += 1

    print(count)
