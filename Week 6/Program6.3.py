'''Write and test a function that determines if a given integer is a prime number. A
prime number is an integer greater than 1 that cannot be produced by multiplying
two other integers.'''

# two other integers. 
def test(num):
    if num == 1:
        print("entered integer is a prime number")
    elif num>1:
        if num % 2 == 0:
            print("entered integer is not a prime number")
        else:
            print("entered integer is a prime number")
    else:
        print("entered integer is not a prime number")
test(int(input("enter a integer: "))) 

