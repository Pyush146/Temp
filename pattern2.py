for i in range(1,6):
	for j in range(1,10):
		if (i>6-j):
			print (" ",end=" ")
		else :
			print ("*",end= " ")
		if(i>j-4) :
			print (" ",end= " ")
		else :
			print ("*", end= " ")
	print ("\r")
for i in range(1,6):
	for j in range(1,10):
		if (i<j):
			print (" ",end=" ")
		else :
			print ("*",end= " ")
		if(i<10-j) :
			print (" ",end= " ")
		else :
			print ("*", end= " ")
	print ("\r")
