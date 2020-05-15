for i in range(0,7) :
	for j in range(0,7) :
		if (i==j or j==6-i) :
			print ("*", end=" ")
		else :
			print (end= " ")
	print ("\r")