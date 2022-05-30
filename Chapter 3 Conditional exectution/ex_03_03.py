# Exercise 3.3: Write a program to a grade to a score

score = input('Enter your grade ') 
fscore = float(score) 
if fscore < 0 or fscore > 1:
    print('Error. Please enter a number between 1.0 and 2.0')
elif fscore >= 0.9: print('A') 
elif fscore >= 0.8: print('B') 
elif fscore >= 0.7: print('C') 
elif fscore >= 0.6: print('D') 
elif fscore < 0.6: print('F') 
