# Rewrite the grade program computegrade that takes a score as its parameter and returns a grade as a string

def computegrade(score):
    if floatscore < 0 or floatscore > 1:
        print('Error. Please enter a number between 1.0 and 2.0')
    elif floatscore >= 0.9:
        print('Your grade is A')
    elif floatscore >= 0.8:
        print('Your grade is B')
    elif floatscore >= 0.7:
        print('Your grade is C')
    elif floatscore >= 0.6:
        print('Your grade is D')
    elif floatscore < 0.6:
        print('Your grade is F')
    x = score
    return x
    print ('Your grade is ', floatscore)

floatscore = float(input('input your score '))
function_call = computegrade(floatscore)

