# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지 모든 시각중에서 3이 하나라도 포함되는 수가 있는 경우를 세기
N = int(input())

cnt = 0
for i in range(N+1):  # 시간
    for j in range(60):  # 분
        for k in range(60):  # 초
            # 문자열 자료형으로 변환한 다음 3이 포함되어있는지 찾기
            time = str(i) + str(j) + str(k)
            if('3' in time):
                cnt += 1

print(cnt)
