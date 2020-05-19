n = int(input())
res=0
for i in range(n):
    tmp=input().split()
    tmp.sort()
    a,b,c = map(int, tmp)
    if a==b and b==c:
        money=10000+1000*a
    elif a==b or a==c:
        money=1000+100*a
    elif b==c:
        money=1000+100*a
    else:
        money=c*100
    if res<money:
        res=money
print(res)