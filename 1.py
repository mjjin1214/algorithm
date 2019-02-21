import sys

sys.stdin = open('input.txt', 'r')


def work(x):
    check_vector[x] -= 1
    if check_vector[x] > 0 or visit_vector[x] == 1:
        return
    visit_vector[x] = 1
    ans.append(x)
    for i in range(len(path_matrix[x])):
        if path_matrix[x][i] == 1:
            work(i)


for t in range(10):
    V, E = map(int, input().split())
    E_list = list(map(int, input().split()))
    path_matrix = [[0 for _ in range(V+1)] for _ in range(V+1)]
    check_vector = [0 for _ in range(V+1)]
    visit_vector = [0 for _ in range(V+1)]
    for e in range(0, len(E_list), 2):
        path_matrix[E_list[e]][E_list[e+1]] = 1
        check_vector[E_list[e+1]] += 1

    ans = []
    for x in range(1, len(check_vector)):
        if check_vector[x] == 0:
            work(x)
    print(f"#{t+1} {' '.join(map(str, ans))}")
