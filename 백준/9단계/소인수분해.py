N = int(input())

# N의 소인수분해 결과를 한줄에 하나씩 오름차순으로 출력
i = 2
while N != 1:
    if N % i == 0:
        N = N // i
        print(i)
    else:
        i += 1
