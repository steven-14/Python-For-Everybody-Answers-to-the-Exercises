'''Exercise 2: Use try except'''

# Input the  hours and pay, then turn those inputs into floating point numbers (decimals)

hours = input("Enter Hours: " )
rate = input("Enter Rate: ")
try:
    fh = float(hours)
    fr = float(rate)
except:
    print("Error, please enter numeric input")
    quit()
    
print(fh, fr)
if fh > 40:
    regularpay = fh * fr
    overtimepay = (fh - 40.0) * (fr * 0.5)
    pay = regularpay + overtimepay
else:
    pay = fh * fr
print("Pay:",pay)

