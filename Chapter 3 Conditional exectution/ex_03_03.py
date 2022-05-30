# Exercise 3.3: Write a program to a grade to a score

score = input('Please enter a score between 0.0 and 1\n')
try:
    floatscore = float(score)
except:
    print('Please enter a numerical value')
 
if floatscore < 0 or floatscore > 1:
        print('Error. Please enter a number between 1.0 and 2.0')
elif floatscore >= 0.9:
        print('Your grade is A')
elif floatscore >= 0.8:
        print('Your grade is B')
elif floatscore >= 0.7:
        print('Your grade is C')
elif floatscore > 0.6:
        print('Your grade is D')
elif floatscore < 0.6:
        print('Your grade is F')
