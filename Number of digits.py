num=int(input("Enter a number upto 5 digits:"))      #Number of digits
if num>=0 and num<=9:
    print("It is a single digit number")
elif num>=10 and num<=99:
    print("It is a double digit number")
elif num>=100 and num<=999:
    print("It is a triple digit number")
elif num>=1000 and num<=9999:
    print("It is a four digit number")
else:
    print("It is a five digit number")

    
