import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())
BREAK_EVEN_POINT = 0

if B > C:
    BREAK_EVEN_POINT = -1
else:
    BREAK_EVEN_POINT = A // (C - B)

print(BREAK_EVEN_POINT)
