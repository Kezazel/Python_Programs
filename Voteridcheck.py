print("VOTE ELIGIBILITY CHECK!\n")
print("Enter your age")
age=int(input())
if(age>=18):
    print("Do you have a voter ID? Y/N")
    ch=input()
    if(ch=='y' or ch=='Y'):
        print("You are eligible to vote")
    elif(ch=='n' or ch=='N'):
        print("You are not eligible to vote")
    else:
        print("Invalid choice")
else:
    print("You are not eligible to vote")





