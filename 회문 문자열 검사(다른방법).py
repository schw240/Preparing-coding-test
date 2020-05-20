n=int(input())
for i in range(n):
    s=input()
    s=s.upper()
    #아래 코드처럼 작성하면 안에 있는 문자를 뒤집어줌
    if s!=s[::-1]:
        print("NO")
    else:
        print("YES")