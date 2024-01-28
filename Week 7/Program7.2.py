''' Write and test three functions that each take two words (strings) as parameters and
return sorted lists (as defined above) representing respectively:
Letters that appear in at least one of the two words.
Letters that appear in both words.
Letters that appear in either word, but not in both.
Hint: These could all be done programmatically, but consider carefully what topic we
have been discussing this week! Each function can be exactly one line.'''

def word1():
    x=input('enter first word: ')
    y=input('enter second word:')
    print("letters in at least one of the words:",least(x,y))
    print('letters in both words',both(x,y))
    print("Letters in either, but not both:",not_in_both(x, y))

def least(x, y):
    return sorted(list(set(x.lower()) | set(y.lower())))

def both(x, y):
    return sorted(list(set(x.lower()) &set(y.lower())))

def not_in_both(x,y):
    return sorted(list(set(x.lower())- set(y.lower())))

word1()
