'''Another way to hide a message is to include the letters that make it up within
seemingly random text. The letters of the message might be every fifth character,
for example. Write and test a function that does such encryption. It should
randomly generate an interval (between 2 and 20), space the message out
accordingly, and should fill the gaps with random letters. The function should
return the encrypted message and the interval used.
For example, if the message is "send cheese", the random interval is 2, and for
clarity the random letters are not random:
send cheese
s e n d c h e e s e
sxyexynxydxy cxyhxyexyexysxye
'''

import random
import string

def message(message_entered):
    interval = random.randint(2, 20)# system takes random interval value between 2 to 20
    letters = string.ascii_letters # system takes randon strings
    encrypted_message = ""
    for char in message_entered:
        encrypted_message += char
        for _ in range(interval):
            encrypted_message += random.choice(letters)
    padding = random.randint(0, interval)#takes 0 spacing  
    for _ in range(padding):
        encrypted_message += random.choice(letters)
    return (encrypted_message, interval)

message_to_encrypt = input("Enter your message to encrypt: ")
encrypted, interval = message(message_to_encrypt)
print("Encrypted message: ",encrypted)
print("Interval: ",interval)
