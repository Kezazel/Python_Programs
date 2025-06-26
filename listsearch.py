numbers= [5,8,12,19,22,35]
tar= int(input("Enter the number to search: "))

for num in numbers:
    if num == tar:
        print(tar,"found in the list.")
        break
else:
    print(tar,"not found in the list.")
