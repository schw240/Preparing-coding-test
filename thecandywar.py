def teacher(N, candy):
    for i in range(N):
        if candy[i] % 2 == 1:
            candy[i] += 1
    return candy


def sharingCandy(N, candy):
    cnt = 0
    while len(set(candy)) != 1:
        children = []
        cnt += 1
        for i in range(N):
            tmp = candy[i] // 2
            candy[i] -= tmp
            children.append(tmp)

        for j in range(-1, N - 1):
            candy[j+1] += children[j]

        teacher(N, candy)
    return cnt


T = int(input())
for i in range(T):
    N, candy = int(input()), list(map(int, input().split(' ')))
    candy = teacher(N, candy)
    ans = sharingCandy(N, candy)
    print(ans)
