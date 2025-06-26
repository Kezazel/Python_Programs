print("Enter the sides of a triangle")
a=float(input())
b=float(input())
c=float(input())
if (a + b > c) and (a + c > b) and (b + c > a): #inequality formula
    if a == b == c:
        print("The triangle is equilateral")
    elif a == b or b== c or a == c:
        print("The triangle is isosceles")
    else:
        print("The triangle is scalene")
else:
    print("Invalid sides!")