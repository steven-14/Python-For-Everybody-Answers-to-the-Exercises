# Exercise 7.3. This version does not calculate the confidence. Soluton 7_3_v1 calculates the confidence also.

"""
Exercise  7.3: 
Modify the program that prompts the user for a file name so that is prints a funny message when the the user types in the exact file name "na na boo boo". the program should
behave normally for all other files which exist and don't exit.
"""

fname = input('Enter the file name: ')
try:
    if fname == 'na na boo boo':
        print('NA NA BOO BOO TO YOU - You have been punk\'d!')
        exit()
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()

count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count += 1

print('There were', count, 'subject lines in', fname)

