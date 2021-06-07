# 1번집은 2번집의 색과 달라야함
# N번 집의 색은 N-1번 집의 색과 달라야함
# i(2~N-1)번의 집의 색은 i-1번, i+1번 집의 색과 같지 않아야한다


# 집의 수 N
N = int(input())

RGB = []
for i in range(N):
    RGB.append(list(map(int, input().split(' '))))

for i in range(1, N):
    # 첫번째 집으로 빨강을 선택하면 그 다음은 파 / 초
    # 두번째 집으로 빨강이 와야한다면 1번째 파랑 초록중 작은값
    RGB[i][0] = min(RGB[i-1][1], RGB[i-1][2]) + RGB[i][0]

    # 초록
    RGB[i][1] = min(RGB[i-1][0], RGB[i-1][2]) + RGB[i][1]

    # 파랑
    RGB[i][2] = min(RGB[i-1][0], RGB[i-1][1]) + RGB[i][2]

    # 모든 집을 칠하는 비용의 최소값 출력
print(min(RGB[N-1]))
