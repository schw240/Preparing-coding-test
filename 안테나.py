# 집의수 N
import sys
input = sys.stdin.readline

N = int(input())
house = list(map(int, input().split()))
house.sort()

print(house[N // 2 - 1])
