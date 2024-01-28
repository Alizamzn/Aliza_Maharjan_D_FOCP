'''Modify the previous program so that it can process any number of values. The input
terminates when the user just pressed "Enter" at the prompt rather than entering a
value.'''

def process_values():
    values = []
    while True:
        value = input("Enter a value (or just press Enter to finish): ")
        if value == "":
            break
        try:
            value = float(value)
            values.append(value)
        except ValueError:
            print("Invalid input. Please enter a number.")
    return values

values = process_values()
print("The processed values are: ", values)
