"""
Exercise 3: Rewrite the guardian code in the above example without two if statements. 
Instead, use a compound logical expression using the or logical operator 
with a single if statement.
"""
# GUARDED PROGRAM
try:
    fhand = open('test_file.txt')
except: print('this file does not exist')

fhand = open('test_file.txt')
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    print(words[2])
   