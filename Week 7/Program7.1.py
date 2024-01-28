'''Write and test a function that takes a string as a parameter and returns a sorted list
of all the unique letters used in the string. So, if the string is cheese, the list
returned should be ['c', 'e', 'h', 's'].'''

def string(s):
    string = sorted(set(s))
    return string

input_string = input("Enter a string: ")
result = string(input_string)
print("Unique sorted letters:", result)



