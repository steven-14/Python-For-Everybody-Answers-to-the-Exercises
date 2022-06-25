# Rewrite pay computation and create a function called computepay which takes two parameters

def computepay(hours, rate):
    if hours_worked > 40:
        regular_pay = rate * hours_worked
        overtime_pay = (hours_worked - 40) * (rate * 0.5)
        gross_pay = regular_pay + overtime_pay
        return gross_pay
        print('if part printed')
    else:
        gross_pay = hours_worked * rate
        return gross_pay
        print('else part printed')

hours = input('Input hours worked\n')
pay = input('Input rate of pay per hour\n')
hours_worked = float(hours)
rate = float(pay)
