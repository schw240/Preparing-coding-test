# 여러개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한장 뽑기
# NXM 형태 카드
# 먼저 뽑고자 하는 카드가 포함되어있는 행선택
# 그 다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드 뽑기
# 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략 세우기

N, M = map(int, input().split(' '))

max_v = 0
for i in range(N):
    graph = list(map(int, input().split(' ')))
    # 여기서 가장 작은수 고르기
    min_v = min(graph)

    # 선택된 카드중 가장 높은 숫자 뽑기
    max_v = max(min_v, max_v)

print(max_v)
