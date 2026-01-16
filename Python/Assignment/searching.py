def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

n = int(input("Enter size of array: "))
arr = []
for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))
key = int(input("Enter element to search: "))

pos1 = linear_search(arr, key)
if pos1 != -1:
    print(f"Linear Search: Element found at position {pos1+1}")
else:
    print("Linear Search: Element not found")

arr.sort()
pos2 = binary_search(arr, key)
if pos2 != -1:
    print(f"Binary Search: Element found at position {pos2+1}")
else:
    print("Binary Search: Element not found")
