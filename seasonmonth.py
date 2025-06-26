month = int(input("Enter month number (1-12):"))

if month in [12,1,2]:
    print("Winter")
elif month in [3,4,5]:
    print("Summer")
elif month in [6,7,8,9]:
    print("Monsoon")
elif month in [10,11]:
    print("Post-Monsoon")
else:
    print("Invalid month number")
