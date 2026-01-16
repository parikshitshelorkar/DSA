array = []
n = int(input("Enter the size of array: "))
#Taking input from user
for i in range (n):
    element = int(input(f"Enter the element {i} : "))
    array.append(element)
print("Array Input Successful..!")
# Printing the array element
for i in range (n):
    print(array[i])
