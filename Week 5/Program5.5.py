'''Last week you wrote a program that processed a collection of temperature readings
entered by the user and displayed the maximum, minimum, and mean. Create a
version of that program that takes the values from the command-line instead. Be
sure to handle the case where no arguments are provided!
'''
import sys
def amd(a):
    max_temp=max(a)
    min_temp=min(a)
    mean_temp=sum(a)/len(a)
    print("maximum temperature is: ",max_temp)
    print("minimum temperature is: ",min_temp)
    print("mean temperature is: ",mean_temp)
x=[float(temperature) for temperature in sys.argv[1:]]
amd(x)     
