# Exercise 2:


# The long solution to ex7.2 
# Use the file name mbox-short.txt as the file name
# Looking for result: 0.75071

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