N = int(input())


def hanoi(N, start, end):
    if N == 1:
        print(start, end)

    hanoi(N-1, start, 6 - (start + end))
    print(N-1, start, end)
    hanoi(N-1, 6 - (start + end), end)


sum = 1
for i in range(N-1):
    sum = sum * 2 + 1
hanoi(N, 1, 3)
