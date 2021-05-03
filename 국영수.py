# N 명의 이름과 국어, 영어, 수학 점수
import sys
input = sys.stdin.readline

N = int(input())
score_list = list()

for i in range(N):
    [name, korean, english, math] = map(str, input().split())
    score_list.append([name, int(korean), int(english), int(math)])

# 국어 내림차순
# 영어 오름차순
# 수학점수 내림차순
# 이름 사전순으로 증가하는 순서
score_list = sorted(score_list, key=lambda x: (-x[1], x[2], -x[3], x[0]))

for score in score_list:
    print(score[0])
