A, B, C = map(int, input().split(' '))

# A 고정비용 B 가변비용 C 노트북 가격
# N * C > A + B * N(노트북 대수)
if C > B:
    print(int(A // (C - B) + 1))
else:
    print(-1)
