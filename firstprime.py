n= int(input("Enter a number:"))
x=n+1

while True:
    for i in range(2, x):
        if x%i== 0:
            break
    else:
        print("First prime number greater than", n, "is", x)
        break
    x += 1
