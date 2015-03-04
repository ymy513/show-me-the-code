from random import randrange
seq = [randrange(10**10) for i in range(100)]
dd = float("inf")
for x in seq:
	for y in seq:
		if x==y:continue
		d=abs(x-y)
		if d<dd:
			xx,yy,dd=x,y,d

xx,yy