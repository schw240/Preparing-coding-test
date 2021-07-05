# 약수의 개수 N
N = int(input())
# 1과 본인을 제외한 약수
factor = list(map(int, input().split(' ')))

max_v = max(factor)
min_v = min(factor)
print(max_v * min_v)
