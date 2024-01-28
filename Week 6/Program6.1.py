'''Write a function that accepts a positive integer as a parameter and then returns a
representation of that number in binary (base 2).
Hint: This is in many ways a trick question. Think!'''

def accept(x):
    a = []
    if x > 0:
        while x != 0:
            a.append(x % 2)
            x = x // 2
        print(a)
    else:
        print("Negative integers are not accepted. Please enter positive integers above 0.")

num = int(input("Enter a positive number: "))
accept(num)
