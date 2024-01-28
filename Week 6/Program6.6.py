'''Write a program that decrypts messages encoded as above.'''


import random
import string

def message(message_entered):
    interval = random.randint(2, 20)# system takes random interval value between 2 to 20
    letters = string.ascii_letters# system takes randon strings
    encrypted_message = ""
    for char in message_entered:
        encrypted_message += char
        for _ in range(interval):
            encrypted_message += random.choice(letters)
    padding = random.randint(0, interval)#takes 0 spacing 
    for _ in range(padding):
        encrypted_message += random.choice(letters)
    return (encrypted_message, interval)

def decrip_message(encrypted_message, interval):
    decrypted = ""
    for i in range(0, len(encrypted_message), interval + 1):
        decrypted += encrypted_message[i]
    return decrypted


message_to_encrypt = input("Enter your message to encrypt: ")
encrypted, interval = message(message_to_encrypt)
print("Encrypted message: ",encrypted)
print("Interval: ",interval)

decrypted_message = decrip_message(encrypted, interval)
print("Decrypted message: ",decrypted_message)
