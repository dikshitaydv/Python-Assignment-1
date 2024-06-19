lst1 = []

n = int(input("Enter number of elements : "))
print("Enter the elements of the list")

for i in range(0, n):
    ele = int(input())

    lst1.append(ele)
sum = 0
for j in lst1:
    sum = sum + int(j)
print("The sum of elements is:",sum)

