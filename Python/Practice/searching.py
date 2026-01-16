import sorting
def LinearSearch(array, item):
    for i in range(len(array)):
        if array[i] == item:
            print("The element found at index: ", i)
        return
    print("Element not found..!")
    pass

def BinarySearch(array, item):
    sorting.AscendingBubbleSort(array, len(array))
    low = 0
    high = (len(array)-1)
    for i in range(len(array)-1):
        mid = ((low + high)//2)
        if array[mid]<item:
            low = mid+1
        elif array[mid]>item:
            high = mid-1
        else:
            print("The element found at index: ", mid)
            return
    print("Element not found..!")
        
        
array = []
def Input():
    n = int(input("Enter the size of array: "))
    for i in range (n):
        element = int(input(f"Enter the Element {i} : "))
        array.append(element)
    print("Input taken Successful..!")
    item = int(input("Enter the element to search: "))
    return item, array

Input()
item, array = Input()
#LinearSearch(array, item)
BinarySearch(array, item)
print("Search operation completed.")
