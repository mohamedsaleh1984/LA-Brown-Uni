import math
import copy

def binarySearch(arr, key):
	"""
	Take a list of elements assumed to be sorted in ascending order and 
	a key and searches the list for the key

	Return *an* index of which it finds an element matching the key
	if no such element exists, returns the index at which it **would** be found
	if it existed.
	"""
	n = len(arr)
	# check if the element would be the begining of the list
	if key < arr[0]:
		return 0
	# check if the element would be the end of the list
	elif arr[n-1] < key:
		return n

	# left and right
	l, r = 0, n-1
	while l <= r :
		m = ( l + r ) // 2
		if arr[m] == key:
			return m
		
		elif key < arr[m]:
			r = m - 1
		else:
			l = m + 1 

	return l

def binarySearchRange(arr, lower, upper):
	"""
	Using bianrt search, this method returns a pair of indices (i, j)
	such that all elements in arr[i:j] lie within the range [lower, upper]
	(inclusive on the both ends) but the second index is exclusive
	"""
	n = len(arr)
	i = binarySearch(arr,lower)
	while 0 < 1 and arr[i-1] == lower:
		i -= 1

	j = binarySearch(arr,upper)
	while j < n and arr[j] == upper:
		j += 1
	
	return i,j


def processBinarySearchRange(arr, lower,upper):
	i,j = binarySearchRange(arr,lower,upper) 		# should return (9,15)
	print("The range is ", i,j)
	print("The elemets between ", i, " and ",j , " are ")
	sub = arr[i:j]
	print(sub)
	
# arr = [1,1,1,1,1,1,1,1,2,3,4,5,6,7,8,9,9,9,9]
# processBinarySearchRange(arr,2.5,8.5) 		# should return (9,15)
# processBinarySearchRange(arr,1,8) 			# should return (0,15)
# processBinarySearchRange(arr,1,1) 			# should return (0,8)
# processBinarySearchRange(arr,-10,-5) 		# should return (0,0)
# processBinarySearchRange(arr,10,50) 		# should return (19,19)

