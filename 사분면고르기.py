# x,y 좌표 양수 또는 음수 가능
x = int(input())
y = int(input())

if(x >= 0 and y >= 0):
    print(1)
elif(x < 0 and y >= 0):
    print(2)
elif(x < 0 and y < 0):
    print(3)
else:
    print(4)
