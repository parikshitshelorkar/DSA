# Bubble sorting

def DescendingBubbleSort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] < array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    print("The Descendingly sorted array is : ", array)

def AscendingBubbleSort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    print("The Ascendingly sorted array is : ", array)

array = []
n = int(input("Enter the size of array: "))
for i in range(n):
    element = int(input(f"Enter the Element {i} : "))
    array.append(element)
print("Input taken Successful..!")

AscendingBubbleSort(array.copy())
DescendingBubbleSort(array.copy())