from validator_collection import validators, checkers, errors

s = input ('What is your email address? ')
'''
index = s.count('@')

if index == 0 or index > 1:
    print("Invalid")
'''

try:
    validators.email(s)
    print('Valid')
except:
    print('Invalid')