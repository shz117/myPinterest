def findSub(A,n,B,m):

	minRange = {}  # hashmap to store minimum subarray that contain all chars in B

	for i in range(m-1,n):    # sliding window: see if A[j:i] contain all chars in B
		if containAll(A[0:i],B,m):
			j = i - m
			while(containAll(A[j:i],B,m)):  # if so slide left border of array until fail to contain all elements
				j = j+1
			minRange[i] = [j,i]
		else:
			minRange[i] = (0,n+2) #just set an impossible range if sub array not found
	ret = n+2
	minr = []
	for k in minRange:
		v = minRange[k]
		if v[1]-v[0]<ret:
			ret = v[1]-v[0]
			minr = v

	if ret>n:   
		print 'No such subarray!'
	else:
		return  minr





def containAll(X,B,m):
	
	# function to tell if subarray X contains all elements in B

	isInB = {}
	numMatched = 0
	for char in B:
		if not char in isInB:
			isInB[char]=1
		else:
			isInB[char]=isInB[char]+1

	for char in X:
		if char in isInB and isInB[char]>0:
			isInB[char]=isInB[char]-1
			numMatched=numMatched+1

	return numMatched == m

A = ['a','b','a','a','a','b']
B =  ['a','a','b']
print findSub(A,len(A),B,len(B))

		


