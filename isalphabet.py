print("Enter a character")
char=input()
if char.isalpha():
    if char.lower() in ['a', 'e', 'i', 'o', 'u']:
        print(char, "is a vowel")
    else:
        print(char, "is a consonant")
else:
    print("Not an alphabet")