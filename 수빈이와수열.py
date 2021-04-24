"""
수열 A를 먼저 쓴다.
그 아래에 정수 수열 A의 해당 항 까지의 평균값을
그 항으로 하는 정수 수열 B


수열 B가 주어질때 수열 A는?
"""

import sys
input = sys.stdin.readline

N = int(input())
B = list(map(int, input().split()))

A = list()
A.append(B[0])
for i in range(1, N):
    A.append(B[i] * (i+1) - sum(A))

for i in range(N):
    print(A[i], end=' ')
