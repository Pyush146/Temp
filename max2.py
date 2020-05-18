d= dict()
l= " "
s= " "
n= int(input("enter number of key"))
for i in range(n):
	print ("enter key")
	dk= input()
	print ("enter value")
	dv= input()
	d[dk]= dv
print(d)
print (" second largest in dictionary")
for i in d:
	for j in d:
		if(d[i]>d[j] and i!= j):
			l=d[i]
for i in d:
	for j in d:
		if(d[i]>d[j] and d[i]<l and i!=j):
			s=d[j]
print (s)