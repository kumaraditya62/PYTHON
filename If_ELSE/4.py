#program to enter any character.if the entered character is in lowercase than convert it to uppercase and if it is in uppercase than convert it to lowercase
ch= input("Enter any character: ")
if(ch>='a' and ch<='z'):
    ch=ch.upper()
    print("The entered character was in uppercase,In lowercase it is: ", ch)
else:
    ch=ch.lower()
    print("The entered character was in lowercase,In uppercase it is: ", ch)