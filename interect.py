#program to find simple intrect and compound intrect of given value
p=float(input("Enter the value of p:"))
r=float(input("Enter the value of r:"))
t=float(input("Enter the value of t:"))
si=p*r*t/100.0
print("Simple interect of given number:",si)
ci=p*(1.0+r/100.0)**t
print("Compound interect of given number:",ci)