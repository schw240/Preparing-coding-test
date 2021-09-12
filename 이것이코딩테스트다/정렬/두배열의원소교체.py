# 두개의 배열 A,B
# N개의 원소, K번의 바꿔치기연산
# 배열 A에 있는 원소 하나와 배열 B에[ 있는 원소 하나를 골라서 두 원소를 서로 바꾸는것을 말한다
# 최종 목표는 배열 A의 모든 원소의 합이 최대가 되도록 하는것

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A의가장 작은 원소, B의 가장 큰 원소 교체
A.sort()
B.sort(reverse=True)

i = 0
while(K != 0):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
        K -= 1
    i += 1

print(sum(A))
