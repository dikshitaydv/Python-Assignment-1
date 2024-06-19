temp = input("Enter CF for celsius to fahrenheit conversion or FC for fahrenheit to celsius conversion:")
if temp == "CF":
    celsius = int(input("Enter the temperature in celsius:"))
    convert = (celsius*1.8)+32
    print(f"Temperature in fahrenheit is {convert}F")
elif temp == "FC":
    fahrenheit = int(input("Enter the temperature in fahrenheit:"))
    conve = (fahrenheit-32)/1.8
    print(f"Temperature in celsius is {conve}C")
else:
    print("Invalid input")







