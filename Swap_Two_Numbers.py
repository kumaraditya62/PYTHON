a = input("Enter first number: ")
b = input("Enter second number: ")
a = int(a)
b = int(b)

print("Before swapping:")
print("a =", a)
print("b =", b)

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)
