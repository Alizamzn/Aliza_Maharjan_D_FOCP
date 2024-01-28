'''Write a program that reads 6 temperatures (in the same format as
before), and displays the maximum, minimum, and mean of the values.
Hint: You should know there are built-in functions for max and min. If
you hunt, you might also find one for the mean.'''

def main():
    b = []
    for i in range(6):
        a = float(input(f"Enter temperature {i + 1}: "))
        b.append(a)
    print(b)

    maximum=max(b)
    minimum=min(b)
    total=sum(b)
    mean=total/len(b)
    print("maximum temperature is: ",maximum)
    print("minimum temperature is: ",minimum)
    print("mean temperature is: ",mean)

main()

    




































