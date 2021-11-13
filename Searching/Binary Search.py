
#Time Complexity : O(log n)
#Space Complexity : O(1)
def BinarySearch(arr,val):
	#The array has to be sorted

	left=0
	right=len(arr)
	while left<right:
		mid=(left+right)//2
		#check val is in mid
		if(arr[mid]==val):
			return mid
		#if val is greater than mid it will be in right side of mid
		elif arr[mid]<val:
			left=mid+1
		#if val is lesser than mid it will be in left side of mid
		else:
			right=mid-1

	return -1


def BinarySearchRecursive(arr,val,left,right):
	#The array has to be sorted
	if right>=left:
		mid=(left+(right-1))//2
		
		if arr[mid]==val:
			return mid
		elif arr[mid]>val:
			return BinarySearchRecursive(arr,val,0,mid-1)
		else:
			return BinarySearchRecursive(arr,val,mid+1,right)

	else:
		return -1

if __name__ == '__main__':
	arr=[5,10,22,64,100,101,102]
	val1=64
	result=BinarySearch(arr,val1)
	if result!=-1:
		print(f"{val1} is present in index {result}")
	else:
		print(f"{val1} is not in the array")

#gfg Link :https://www.geeksforgeeks.org/binary-search/