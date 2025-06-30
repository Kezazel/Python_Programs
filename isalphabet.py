print("Enter a character")
char=input()
vowels=[97,101,105,111,117,65,69,73,79,85]
if ord(char)>=97 and ord(char)<=122 or ord(char)>=65 and ord(char)<=90:
    if ord(char) in vowels:
        print("Vowels")
    else:
        print("Consonants")
else:
    print("Error")