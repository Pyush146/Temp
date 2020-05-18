def replace(n):
	n+= calc(n)
	return n
def calc(n):
	r=0
	d=1
	if (n==0):
		r+= 5*d
	while n>0 :
		if n%10==0 :
			r+= 5*d
		n//=10
		d*=10
	return r
a= int(input())
print (replace(a))