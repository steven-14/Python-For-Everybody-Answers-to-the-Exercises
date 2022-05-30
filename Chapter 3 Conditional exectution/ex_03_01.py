'''Exercise 1: Rewrite your pay computation to give the employee 1.5 
times the hourly rate for hours worked above 40 hours.'''

# Input the  hours and pay, then turn those inputs into floating point numbers (decimals)
hours = input('Input hours worked\n')
pay = input('Input rate of pay per hour\n')
hours_worked = float(hours)
rate_of_pay = float(pay)

''' Use an if else conditional statement to calculate and print the regular pay 
or regular pay + overtime'''
if hours_worked > 40:
    regular_pay = rate_of_pay * hours_worked
    overtime_pay = (hours_worked - 40) * (rate_of_pay * 0.5)
    gross_pay = regular_pay + overtime_pay
else:
    gross_pay = hours_worked * rate_of_pay
print('Pay:', gross_pay)
