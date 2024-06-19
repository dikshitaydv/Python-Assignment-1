str1 = input("Enter any string:")
dict1 = {}

for i in str1:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1


print(f"Count of all characters in {str1} is :\n ",str(dict1))




