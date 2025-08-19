#program to enter a decimal number calculate and dislpay its binary equivalent of this number
decimal_num=int(input("Enter a decimal number: "))
binary_num = 0
i=0
while(decimal_num!=0):
    remainder = decimal_num % 2
    binary_num = binary_num + remainder * (10 ** i)
    decimal_num = decimal_num // 2
    i += 1
    print("Binary equivalent is: ", binary_num)