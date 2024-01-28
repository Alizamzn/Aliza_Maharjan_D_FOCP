'''Computers are commonly used in encryption. A very simple form of encryption
(more accurately "obfuscation") would be to remove the spaces from a message
and reverse the resulting string. Write, and test, a function that takes a string
containing a message and "encrypts" it in this way.
'''

def my_encrypted_message(message_to_encrypt):
    #remove all whitespaces
    message_with_no_spaces = message_to_encrypt.replace(" ","")
    
    #reverse the string obtained after removing white spaces
    message_after_encryption = message_with_no_spaces[::-1]
    
    return message_after_encryption

unecrypted_message = input("Enter your message to encrypt: ")

encryptedMessage = my_encrypted_message(unecrypted_message)

print(f"your encrypted message is: {encryptedMessage}")
