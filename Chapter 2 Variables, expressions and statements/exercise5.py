# py4e chapter 2 exercise 5
'''Exercise 5: Write a program which prompts the user for a Celsius temperature,
convert the temperature to Fahrenheit, and print out the converted temperature.'''


prompt = (float(input('Input the temperature in degrees celcius\n')))
far = float(prompt * 1.8 + 32)
print ('Converted to fahrenheight that is', far)
