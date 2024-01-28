'''Write and test a function that takes an integer as its parameter and returns the
factors of that integer. (A factor is an integer which can be multiplied by another to
yield the original).'''

def num(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)
num(int(input("enter a number: "))) 
