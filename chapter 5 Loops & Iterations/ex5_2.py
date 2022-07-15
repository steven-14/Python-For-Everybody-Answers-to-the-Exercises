'''
Exercise 2: Write another program that prompts for a list of numbers as above 
and at the end prints out both  
the maximum 
and minimum of the numbers 
instead of the average.
'''
# From C5 video 5 Worked Exercise: 5.2
largest = None
smallest = None
while True:
    num = input('Enter your number: ')
    if num == 'done':
        break
    else:
        try:
            n = int(num)
        except:
            print('Invalid input')

    if largest is None:
        largest = n
    elif n > largest:
        largest = n

    if smallest is None:
        smallest = n
    elif n < smallest:
        smallest = n

print('Maximum is',largest)
print('Minimum is',smallest)
