def ins(l1,l2):
	return list(set(l1) & set(l2))
l1=list(input())
l2= list(input())
print (ins(l1,l2))