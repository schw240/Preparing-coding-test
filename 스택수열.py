n = int(input())

stack = []
res = []
count = 1

# 원래 숫자는 1 ~ n까지
for i in range(1, n+1):
    data = int(input())
    # count가 입력받은 data랑 같아질때까지 count를 push
    # push는 res에 + 기호 추가
    while count <= data:
        res.append("+")
        stack.append(count)
        count += 1
    # 입력받은 data와 stack의 최 상단 확인
    if data == stack[-1]:
        # 둘이 같다면 pop을 해야함
        # res에 - 추가
        res.append("-")
        stack.pop()
    else:
        print("NO")
        exit(0)

for i in range(len(res)):
    print(res[i])
