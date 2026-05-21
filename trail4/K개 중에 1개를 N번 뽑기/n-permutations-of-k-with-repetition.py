K, N = map(int, input().split())

arr = []

def choose(d):
    if d == N:
        print(*arr)
        return

    for i in range(1, K + 1):
        arr.append(i)
        choose(d + 1)
        arr.pop()

choose(0)