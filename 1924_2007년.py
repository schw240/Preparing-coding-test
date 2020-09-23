months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

x, y = map(int, input().split())

res = 0

for i in range(x-1):
    res += months[i]
    #print(res)
res = res + y
#print(res)
res = res % 7
#print(res)
print(days[res])

