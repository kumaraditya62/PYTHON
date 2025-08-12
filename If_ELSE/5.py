#A company decides to give bonus to employees on diwali.A 5% bonus on salary is given to male employeesand a 10% bonus on salary is given to the female employees.
#write program to enter salary of the employees and sex of the employee and calculate the bonus.employee is less than 10000 then the employee gets an extra 2% bonus on salary.
# calculate the bonus that has to be given to the employee and display the salary that the employee will get after bonus.

ch=input("Enter the sex of the employee (M/F): ")
ch=int(input("Enter the salary of the employee: "))
if ch == 'M':
    bonus = 0.05 * ch
else:
    bonus = 0.10 * ch
    amt_to_be_paid = ch + bonus
    print("The bonus is:", bonus)
    print("******************")
    print("The amount to pay is:", amt_to_be_paid)
