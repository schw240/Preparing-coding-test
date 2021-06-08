n = int(input())

triangle = []
for i in range(n):
    triangle.append(list(map(int, input().split(' '))))

for i in range(1, n):
    for j in range(len(triangle[i])):
        # 대각선 왼쪽만 올수 있는 경우
        if j == 0:
            triangle[i][j] += triangle[i-1][j]
        # 대각선 오른쪽만 올수있는 경우
        elif j == i:
            triangle[i][j] += triangle[i-1][j-1]
        # 둘다 가능한 경우
        else:
            triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])


print(max(triangle[n-1]))
