#This calculates the factorial of a number using a while loop
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        i = 2
        while i <= n:
            fact *= i
            i += 1
        return fact

num = 5
print("factorial:", factorial(num))
