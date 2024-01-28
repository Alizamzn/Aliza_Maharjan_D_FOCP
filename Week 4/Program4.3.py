'''Modify your "greetings" program so that the first letter of the name entered is
always in uppercase with the rest in lowercase. This should happen even if the user
entered their name differently. So if the user entered arthur, ARTHUR, or even
arTHur the name should be displayed as Arthur.'''

def string1(name):
    name = name.lower()
    name = name.capitalize()
    print("hello,",name, 'nice to meet you')
    
a = input("Enter your name: ")
string1(a) 
