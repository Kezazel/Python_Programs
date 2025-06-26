num = int(input("Enter a number:"))
og=num
rev=0

while num>0:
    dig=num%10
    rev=rev*10+dig
    num//=10

if og==rev:
    print("Palindrome!")
else:
    print("Not a palindrome!")
