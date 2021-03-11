n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], input_data[1]))

array = sorted(array, key=lambda student: student[1])  # 점수 기준 정렬

for student in array:
    print(student[0], end=' ')
