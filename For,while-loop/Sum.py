#program to calculate the sum of numbers from m to n
m = int(input("Enter the starting number (m): "))
n = int(input("Enter the ending number (n): "))
s=0
while(m <= n):
    s= s + m
    m = m + 1
    print("The sum of numbers from", m, "to", n, "is:", s)