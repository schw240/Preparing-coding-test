import sys
from itertools import permutations

# 수의 개수
N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split(" ")))
op = list(map(int, sys.stdin.readline().split(" ")))
ops = []

for i in range(4):
    for k in range(op[i]):
        ops.append(i)

minimum = sys.maxsize
maximum = -1 * sys.maxsize

for com in set(permutations(ops, N-1)):
    answer = A[0]
    for i in range(len(com)):
        if com[i] == 0:
            answer += A[i+1]
        elif com[i] == 1:
            answer -= A[i+1]
        elif com[i] == 2:
            answer *= A[i+1]
        else:
            # 둘이 부호가 다르면
            if answer * A[i+1] < 0:
                answer = -1 * (abs(answer) // abs(A[i+1]))
            else:
                answer = answer//A[i+1] 

    minimum = min(minimum, answer)
    maximum = max(maximum, answer)

print(maximum)
print(minimum)
