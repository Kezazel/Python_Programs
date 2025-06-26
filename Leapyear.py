print("Enter the year")
yr=int(input())
if (yr%4==0) and (yr%100!=0):
    print("Leap year!")
elif(yr%400==0):
    print("Leap year!")
else:
    print("Not a leap year!")