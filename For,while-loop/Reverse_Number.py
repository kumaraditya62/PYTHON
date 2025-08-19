num = int(input("Enter the number: "))
print("The reversed number is:", end=" ")

while(num != 0):
    temp = num % 10
    print(temp, end=" ")
    num = num / 10
