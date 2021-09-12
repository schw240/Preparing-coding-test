N = int(input())

arr = []
for i in range(N):
    arr.append((input().split(' ')))

# 학생 정보는 학생의 이름과 성적으로 구분
# 성적이 낮은 순서대로 학생 이름 출력
arr = sorted(arr, key=lambda x: x[1])

for lst in arr:
    print(lst[0], end=' ')
