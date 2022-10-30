"""
Exercise 3: 
Write a program to read through a mail log, 
build a histogram using a dictionary 
to count how many messages have come from each email address, 
and print the dictionary.
"""

dictionary_days = dict()                       # Initializes the dictionary
fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    else:
        if words[1] not in dictionary_days:
            dictionary_days[words[1]] = 1       # First entry
        else:
            dictionary_days[words[1]] += 1      # Additional counts

print(dictionary_days)
    


