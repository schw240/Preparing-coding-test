import sys
n = int(input())
l = []

for _ in range(n):
    l.append(int(sys.stdin.readline()))

l.sort()

print('%d' % (round(sum(l)/n, 0)))
print(l[n//2])

x = {}

for i in l:
    if i in x:
        x[i] += 1
    else:
        x[i] = 1
x = sorted(x.items(), key=lambda x: x[1], reverse=True)

if n != 1:
    if x[0][1] == x[1][1]:
        print(x[1][0])
    else:
        print(x[0][0])
else:
    print(x[0][0])

print(max(l) - min(l))
