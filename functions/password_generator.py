import random
import string

'''
    collects random characters equivalent to length and concatenate as a string
'''

def password(length, digits = True, alphabets = True):
    characters = str()
    if alphabets:
        characters += string.ascii_letters 
    if digits:
        characters += string.digits
    
    if len(characters) == 0:
        raise BaseException('Error!!! Wrong options given')

    return str().join([random.choice(characters) for x in range(length)])
