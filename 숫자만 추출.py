s=input()
res=0
for x in s:
    #하나하나씩 s안에있는 문자를 x로 접근
    if x.isdigit():
        res=res*10+int(x)

print(res)
cnt=0
for i in range(1,res+1):
    if res%i==0:
        cnt+=1

print(cnt)