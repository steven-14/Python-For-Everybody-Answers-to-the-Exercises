# To round a number, we must set variable x to floating point number input
x = float(input('Input hours worked\n'))
y = float(input('Input rate of pay per hour\n'))
# Round the result in gross to 1 decimal point.
gross = round((x * y),1)
print('Gross pay = £',gross)
