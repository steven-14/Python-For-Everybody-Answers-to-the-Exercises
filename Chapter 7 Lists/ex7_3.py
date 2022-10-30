# Exercise 3:

def punked():
   print("NA NA BOO BOO TO YOU - You have been punk'd!")

fname = input("Enter file name: ")
count = 0
num = 0
try:
    if fname == 'na na boo boo':
        punked()
        exit()
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        num += float(line[line.find(' '):])
        count += 1
print('Average spam confidence:', num/count)

# actual result: 0.7507185185185187

