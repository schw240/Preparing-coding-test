A = int(input())
B = int(input())
C = int(input())

num = str(A * B * C)

for i in range(10):
    cnt = 0
    for j in range(len(num)):
        if int(num[j]) == i:
            cnt += 1
    print(cnt)
