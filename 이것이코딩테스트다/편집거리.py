# A = input()
# B = input()

# 문자열 A를 편집해서 B로 만들기
# 문자열을 편집할때는 세 연산중 하나씩 선택해서 이용
# 1. 삽입: 특정 위치에서 하나의 문자 삽입
# 2. 삭제: 특정 위치의 문자 하나 삭제
# 3. 교체: 특정 위칭 있는 하나의 문자를 다른 문자로 교체

# 편집 거리란 문자열 A를 편집해서 문자열 B로 만들기 위해 사용한 연산의 수

# cat
# cut
# 1

# sunday
# saturday
# 3

A = "cat"
B = "cut"

A = list(A)
B = list(B)
# 이중배열
dp = [[0] * (len(B)+1) for _ in range(len(A)+1)]

# 만든 이중배열을 반복문을 따라 비교하면서 점수 확인
# 점화식?
# 같으면 0 다르면 + 1 그다음 이전과 비교? 위, 아래값중 최소값 + 1
#   c a t
# c 0 1 1
# u 1 2 2
# t 2 3 2 -> 이래서 1인가

for i in range(1, len(A)+1):
    for j in range(1, len(B)+1):
        # print(dp)
        # 둘이 알파벳이 같다면
        # print(A[i], B[j])
        if A[i-1] == B[j-1]:
            # 같으면 최소값? 만약 이전값이 없다면 0
            # if dp[i][j] == 0:
            #     dp[i][j] = 1
            # 이전값이 있다면 비교해서 최소값?
            dp[i][j] = min(dp[i-1][j], dp[i][j-1])
            # dp[i][j] = dp[i-1][j-1]
        # 다르다면
        else:
            # 왼쪽값, 위의값, 대각방향중 최소값 + 1
            dp[i][j] = min(dp[i][j-1] + 1, dp[i-1][j] + 1)

print(dp)
# print(dp[len(A)-1][len(B)-1])
