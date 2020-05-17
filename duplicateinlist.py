l=[]
n=int(input("enter number "))
for i in range(n) :
	a=int(input())
	l.append(a)
def remove(l):
	fl=[]
	for num in l :
		if num not in fl :
			fl.append(num)
	return fl
print (remove(l))