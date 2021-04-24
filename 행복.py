"""
행복감과 성적 차이 관계

N 명의 학생들의 점수가 주어졌을 때, 가장 높은 점수와 가장 낮은 점수의 차이를 구하는 프로그램
"""

import sys
input = sys.stdin.readline

N = int(input())
score_list = list(map(int, input().split()))

print(max(score_list) - min(score_list))
