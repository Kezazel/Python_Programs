print("Enter three numbers")
n1=int(input())
n2=int(input())
n3=int(input())
if(n1>n2):
    if(n1>n3):
        print(n1,"is the largest number.")
    else:
        print(n3,"is the largest number.")
else:
    if(n2>n3):
        print(n2,"is the largest number.")
    else:
        print(n3,"is the largest number.")
