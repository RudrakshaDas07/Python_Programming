num=int(input("Enter a number here:"))        #Palindrome no.
temp=num
rev=0
while num>0:
  digit=num%10
  rev=rev*10+digit
  num=num//10
if rev==temp:
  print("It is a Palindrome number")
else:
  print("It is not a Palindrome number")