#this is your fibonacci dataset based

def F(n):
	if n==10 or n==20:
		return 10
	elif n == 0:
		return 0
	else:
		return F(n-10) + F(n-20)

x = 0
ls=[]
for i in range(10):
	x+=10
	ls.append(F(x))

print(ls)
