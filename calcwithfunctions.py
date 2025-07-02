def multi(num1,num2):
    "This does multiplication"
    ans=num1*num2
    return ans

def add(num1,num2):
    "This does addition"
    ans=num1+num2
    return ans

def sub(num1,num2):
    "This does subtraction"
    ans=num1-num2
    return ans

def div(num1,num2):
    "This does divison"
    if(num2==0):
        print("Division not possible")
        return
    else:
        ans=num1/num2
    return ans

choice='y'
while choice=='y' or choice=='Y':

    num1=int(input("Enter the first number"))
    num2=int(input("Enter the second number"))

    ch=input("Enter choice")
    if ch=='+':
        ans=add(num1,num2)
        print(ans)
    elif ch=='-':
        ans=sub(num1,num2)
        print(ans)
    elif ch=='*':
        ans=multi(num1,num2)
        print(ans)
    elif ch=='/':
        ans=div(num1,num2)
        print(ans)
    else:
        print("Error")
choice=int(input("Enter your choice")) #belloooo