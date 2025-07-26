num=int(input("Enter a number here:"))             #Prime no.
if num<=1:
  print("It is not a Prime number")
else:
  for i in range(2,num):
    if num%i==0:
       print("It is not a Prime number")
       break
  else:
    print("It is a Prime number")
       