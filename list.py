def ins(l1,l2):
	return list(set(l1) & set(l2))
l1=[]
l2= []
n= int(input(" enter number of elements :"))
for i in range(n) :
	a=int(input())
	l1.append(a)
for i in range(n) :
	b=int(input())
	l2.append(b)
print (ins(l1,l2))