n = int(input())

cnt = 0

def bu(length):
    global cnt

    if length == n:
        cnt += 1
        return

    if length > n:
        return

    for i in range(1, 5):
        bu(length + i)

bu(0)

print(cnt)