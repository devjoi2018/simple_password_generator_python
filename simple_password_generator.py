# This code is part of the tests that I have been doing with Github Copilot.

# Program that generates passwords randomly
# The length of the password must be requested from the user through the console
# The user should be asked if they want to include special characters in the opassword
# If the user selects 'y', a password must be generated with special characters and with uppercase lowercase letters and numbers randomly
# If the user chooses 'n', a password must be generated with uppercase lowercase letters and numbers randomly

import random
import string
import sys
import os

def main():
    print('RANDOM PASSWORD GENERATOR')
    
    print('Select an option: ')
    print('1. Generate random password')
    print('2. Generate password with special characters')
    print('3. Generate password with uppercase lowercase letters and numbers')
    option = input('Enter your option:')
    if option == '1':
        length = input('Enter the password length: ')
        password = generate_password(length)
        print('Password generado: ' + password)
    elif option == '2':
        length = input('Enter the password length: ')
        password = generate_password_especial_character(length)
        print('Password generado: ' + password)
    elif option == '3':
        length = input('Enter the password length: ')
        password = generate_password_uppercase_lowercase(length)
        print('Generated password: ' + password)
    else:
        print('Enter a valid option')

def generate_password(longitud):
    password = ''
    for i in range(int(longitud)):
        password += random.choice(string.ascii_letters + string.digits)
    return password

def generate_password_especial_character(longitud):
    password = ''
    for i in range(int(longitud)):
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)
    return password

def generate_password_uppercase_lowercase(longitud):
    password = ''
    for i in range(longitud):
        password += random.choice(string.ascii_letters + string.digits)
        if i % 2 == 0: password += random.choice(string.ascii_uppercase)
        else: password += random.choice(string.ascii_lowercase)
    return password

if __name__ == '__main__':
    main()