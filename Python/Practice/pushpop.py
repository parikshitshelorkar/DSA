arr = []
def pushElement():
	n = int(input("How many elements you want to append: "))
	for i in range(n):
		element = int(input(f"Enter the elements: {i+1} -->"))
		arr.append(element)
	print("The Array after Insertion: ", arr)
		
	return arr

def popElement(arr):
	num = int(input("Enter the index of number to be deleted: "))
	arr.pop(num)

pushElement()
popElement(arr)

print("Array after Deletion is : ", arr)
