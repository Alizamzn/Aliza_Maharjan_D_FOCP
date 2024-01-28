'''Write a program that prompts a user to enter a temperature in Celsius, and then
displays the corresponding temperature in Fahrenheit, like so:
Enter a temperature in Celsius: 32.5
32.5C is equivalent to 90.5F.'''

C = float(input('Input the temperature in celsius: '))
F = C * (9 / 5) + 32
print(f'Hello the temperature is {F} degree Fahrenheit.!')
