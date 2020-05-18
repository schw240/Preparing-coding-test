n , a = int(input()) , list(map(int , input().split()))

def digit_sum(x):
    sum = 0
    #밑에 처럼 작성하면 x로 받아온 숫자를 문자열로 받아옴
    for i in str(x):
        #각 자리수를 다시 int로 바꿔서 더해줌
        sum+=int(i)
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

