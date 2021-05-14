# 삼각형 크기 n
n = int(input())
triangle = []
for i in range(n):
    nums = [0]
    tmp = list(map(int, input().split(' ')))
    tmp.append(0)
    nums.extend(tmp)
    triangle.append(nums)

# print(triangle)

# 바로위 또는 왼쪽 위 또는 둘중 큰값
for i in range(1, n):
    for j in range(i+1):
        triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])

print(triangle, "triangle")
print(max(triangle[n-1]))

# # 둘째줄부터 시작
# for i in range(1, n):
#     # 각 줄에서 값 하나씩 확인
#     for j in range(i+1):
#         # 왼쪽인 경우
#         if j == 0:
#             triangle[i][j] += triangle[i-1][j]
#         # 오른쪽인 경우
#         elif j == i:
#             triangle[i][j] += triangle[i-1][j-1]
#         # 가운대 값들인 경우
#         else:
#             triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])

# # print(triangle, "triangle")
# print(max(triangle[n-1]))
