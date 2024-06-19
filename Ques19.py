str1 = input("Enter any string:")

punc_str = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

for ele in str1:
    if ele in punc_str:
        str1 = str1.replace(ele, "")

print("The string after removing all punctuations is: " + str1)



