def fact(num):
    if num<0:
        print("Entered number is negative")
        return "invalid"
    elif num == 0 or num == 1:
        return 1
    else:
        num = num * fact(num-1)
    return num

num= int(input("Enter the number:"))
result=fact(num)
print(f"Factorial of {num} is ",result)


