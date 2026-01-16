n = int(input("Enter the number of employees: "))
salaries = []

for i in range(n):
    salary = float(input(f"Enter salary of employee {i+1}: "))
    salaries.append(salary)

def selection_sort(sal_list):
    arr = sal_list.copy()
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def bubble_sort(sal_list):
    arr = sal_list.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

selection_sorted = selection_sort(salaries)
bubble_sorted = bubble_sort(salaries)

print("\nOriginal Salaries:", salaries)
print("\nSelection Sort (Ascending):", selection_sorted)
print("Bubble Sort (Ascending):", bubble_sorted)

# Top 5 highest salaries in descending order
top_5_salaries = sorted(salaries, reverse=True)[:5]
print("\nTop 5 Highest Salaries (Descending):", top_5_salaries)