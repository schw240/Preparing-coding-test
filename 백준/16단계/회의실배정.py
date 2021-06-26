N = int(input())

# N개의 회의에 대하여 회의실 사용표 만들기
# 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 최대 개수
using = []
for i in range(N):
    start, end = map(int, input().split(' '))
    using.append([start, end])

# 회의가 끝나는 동시에 다음 회의가 시작될 수 있음
# 3 3
# 3 3 과 같은 값이 들어오는 경우 output이 2가 되야함

# 따라서 빨리 끝나는 회의 순서대로 정렬을 해야한다.(끝나는 시간 정렬)

# 하지만 끝나는 시간만 정렬할 경우
# 2 2
# 1 2 의 경우 답이 2이지만 끝나는 시간만 정렬하면 1이 된다.
# 따라서 시작시간도 시작하는 시간도 오름차순으로 정렬해주어야함

using.sort(key=lambda x: x[0])
using.sort(key=lambda x: x[1])

cnt = 0
last = 0

for i in range(N):
    start, end = using[i]

    if start >= last:
        cnt += 1
        last = end


print(cnt)
