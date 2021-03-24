# 모험가 N명
# 공포도 X면 X명 이상
# 최대의 그룹

N = int(input())

mans = list(map(int, input().split()))
mans.sort()

group_num = 0  # 그룹수
cnt = 0  # 인원수
for i in range(len(mans)):
    cnt += 1
    # 공포도와 인원수 비교해서 인원수가 크거나 같으면
    if cnt >= mans[i]:
        group_num += 1
        cnt = 0

print(group_num)
