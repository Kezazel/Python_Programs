print("Enter 1 to convert fahrenheit to celsius\nEnter 2 to convert celsius to fahrenheit")
ch=int(input())
if(ch==1):
        print("Enter fahrenheit value")
        fah=float(input())
        cel=(5.0/9.0)*(fah-32.0)
        print("Corresponding celsius value is", cel)
elif(ch==2):
        print("Enter celsius value")
        cel = float(input())
        fah = ((9.0/5.0)*cel) + 32.0
        print("Corresponding fahrenheit value is", fah)
else:
        print("Invalid")

