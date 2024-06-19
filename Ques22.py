lst = []

n = int(input("Enter number of elements : "))
print("Enter the elements of the list")
for i in range(0, n):
    element = int(input())

    lst.append(element)

maximum = max(lst)
minimum = min(lst)
print(f"The maximum value is {maximum} and the minimum value is {minimum}")



