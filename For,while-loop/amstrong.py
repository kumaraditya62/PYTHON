#program to find whether the given number is an Armstrong number or not
n=int(input("Enter a number: "))
s=0
num=n
while(n > 0):
    r=n % 10
    s=s + r**3
    n=n /10
if(s == num):
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")