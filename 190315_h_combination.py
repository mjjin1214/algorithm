def recom(k, l):
    global L, K
    if l >= L or k > K:
        if l == L:
            print(answer)
        return

    recom(k+1, l)
    answer[l] = k
    recom(k, l+1)

K = 5
L = 3
answer = [0]*L
recom(1, 0)
