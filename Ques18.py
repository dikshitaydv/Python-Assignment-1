str1 = input("Enter first string:")
str2 = input("Enter second string:")

str1 = str1.lower()
str2 = str2.lower()

if (len(str1) == len(str2)):
    sort_str1 = sorted(str1)
    sort_str2 = sorted(str2)

    if(sort_str1 == sort_str2):
        print(f"{str1} and {str2} are anagram")
    else:
        print(f"{str1} and {str2} are not anagram.")

else:
    print(f"{str1} and {str2} are not anagram.")