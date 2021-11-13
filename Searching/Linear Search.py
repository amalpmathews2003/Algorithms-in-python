#Simple Linear Search
#Time Complexity : O(n)
#Space Complexity : O(1)
def LinearSearch(arr,val):
	#Iterative Approch
	for i in range(0,len(arr)):
		if(arr[i]==val):
			return i
	return -1
	"""
	Looping through the array from 0 to len(arr)
	till we find the val.If we find the val,return its position

	Sorted array if not required here
	"""
def LinearSearchRecursive(arr,val,left,right):
	if right<left:
		return -1
	if arr[left]==val:
		return left
	if arr[right]==val:
		return right

	return LinearSearchRecursive(arr,val,left+1,right-1)

def OptimisedLinearSearch(arr,val):
	left=0
	right=len(arr)-1

	for left in range(right):
		if(arr[left]==val):
			return left
		if arr[right]==val:
			return right
		left+=1
		right-=1
	return -1

	"""
	The problem with simple linear search is that when we wat to search the
	last element it will have to loop over all elements.This can be resolved
	by Optimised Linear Search 

	Approch:
		We start looping from left and right sides of the array simultaneously
		till we find the val
	"""


if __name__ == '__main__':
	arr=[10,2,435,92,-1,9]
	val1=-2
	result=LinearSearch(arr,val1)
	if result!=-1:
		print(f"{val1} is present in index {result}")
	else:
		print(f"{val1} is not in the array")
	
	
"""
Problem: Given an array arr[] of n elements, write a function to search a given element x in arr[].

Input : arr[] = {10, 20, 80, 30, 60, 50, 
                     110, 100, 130, 170}
          x = 110;
Output : 6
Element x is present at index 6

Steps :
	1)Start from the leftmost element of arr[] and one by one compare x with each element of arr[]

	2)If x matches with an element, return the index.

	3)If x doesn’t match with any of elements, return -1.
"""

#gfg Link :https://www.geeksforgeeks.org/linear-search/