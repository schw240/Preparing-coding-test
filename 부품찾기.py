# 특정 수가 한번이라도 등장하는지 검사하면 되므로 집합 자료형을 이용해도 됌

n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')
