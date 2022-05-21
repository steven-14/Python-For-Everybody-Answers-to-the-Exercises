# -*- coding: utf-8 -*-
"""
Created on Thu May 19 22:22:02 2022

@author: steven174
"""

'''inp = input('What is your name?')
print('Hello',inp)'''

# To round a number, we must set variable x to floating point number input
x = float(input('Input hours worked\n'))
y = float(input('Input rate of pay per hour\n'))
# Round the result in gross to 1 decimal point.
gross = round((x * y),1)
print('Gross pay = £',gross)
