"""
알파벳 대문자로 적은 다음
알파벳에 대응하는 숫자로 바꾸고 각 숫자와 오른쪽 숫자와 더한 것을 밑에 적는다.
더한 숫자가 10이 넘으면 일의 자리 수만 남긴다.
이 과정을 반복하여 숫자가 2개만 남을때 두 사람의 궁합이 좋을 확률이 됨
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A, B = map(str, input().split())

alp = [3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1,
       3, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

A_B = ''
min_len = min(len(A), len(B))

for i in range(min_len):
    A_B += A[i] + B[i]

# if len(A) > len(B):
#     A_B += A[min_len:]
# elif len(A) < len(B):
#     A_B += B[min_len:]
A_B += A[min_len:] + B[min_len:]

lst = [alp[ord(i) - ord('A')] for i in A_B]

for i in range(N + M - 2):
    for j in range(N + M - 1 - i):
        lst[j] += lst[j+1]
        lst[j] = lst[j] % 10

print("{}%".format(lst[0] * 10 + (lst[1])))
