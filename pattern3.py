for i in range(3,0,-1):
	for j in range(0,5):
		if 2*i-1>j :
			if j%2==0 :
				print (i,end=" ")
			else :
				print ("*",end=" ")
		else :
			print (" ",end=" ")
	print ("\r")
for i in range(1,4):
	for j in range(0,5):
		if 2*i-1>j :
			if j%2==0 :
				print (i,end=" ")
			else :
				print ("*",end=" ")
		else :
			print (" ",end=" ")
	print ("\r")
		