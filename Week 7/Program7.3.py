'''Write a program that manages a list of countries and their capital
cities. It should prompt the user to enter the name of a country. If the
program already "knows" the name of the capital city, it should display
it. Otherwise it should ask the user to enter it. This should carry on
until the user terminates the program (how this happens is up to you).
Note: A good solution to this task will be able to cope with the country
being entered variously as, for example, "Wales", "wales", "WALES" and
so on.  '''

country=input("enter a country : ")
country_stored={'nepal':'kathmandu','japan':'tokyo','germany':'berlin',
                'russia':'muscow','us':"washington dc"}
if country in country_stored:
    print("capital of",country,"is",country_stored[country])
else:
    capital=input('enter the capital of ')
    country_stored[country]:capital
    print("capital of",country,"is",country_stored[country])
