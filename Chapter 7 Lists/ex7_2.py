"""
Exercise 2:
Figure out which line of the above program is still not
properly guarded. See if you can construct a text file which causes the
program to fail and then modify the program so that the line is properly
guarded and test it to make sure it handles your new text file.

Use the file name mbox-short.txt as the file name
Looking for result: 0.75071
"""

fname = input("Enter file name: ")
fhand = open(fname)
count = 0
total = 0

for line in fhand:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        space = line.find(' ')
        fval = float(line[space:]) # floating point value
        total += fval
        count += 1
print('Average spam confidence for solution v3 is:', total/count)

# actual result: 0.7507185185185187
