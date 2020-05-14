
n = int(iinput())
a = list(map(int , input().split()))

ave = round(sum(a)/n)
min = 100000000
for idx , x in enumerate(a):
	tmp = abs(x-ave)
	if tmp<min:
		min = tmp
		score = x
		res = idx + 1
	elif tmp == min:
		if x > score:
			score=x
			res=idx+1

print(ave , res)