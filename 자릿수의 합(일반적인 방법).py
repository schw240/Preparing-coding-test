n , a = int(input()) , list(map(int , input().split()))

def digit_sum(x):
    sum = 0
    while x>0:
        sum+=x%10
        x=x//10

    return sum

max=0

#리스트는 이런 방식으로도 접근 가능
#리스트 안에 있는 원소 하나하나씩 꺼내옴
for x in a:
    total = digit_sum(x)
    if max < total:
        max = total
        res = x
print(x)
