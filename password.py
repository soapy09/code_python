import random

#Program Introduction
print("Welcome to our password generating app!")

# Set password length
pwd_length= int(input("Enter the length of the password: "))

#Password Criteria
lowercase = list(range(97, 123))
uppercase = list(range(65, 91)) #range never includes the last value
digits = list(range(48, 58))
special = list(range(33, 48)) + list(range(58, 65)) + list(range(91 , 97)) + list(range(123, 127))

pwd_symbols = lowercase.copy() #list of possible characters for our password

has_upper = input("Include uppercase characters? (y/n): ")
if has_upper == 'Y' or has_upper == 'y':
    pwd_symbols.extend(uppercase)
    #pwd_symbols = pywd_symbols + uppercase

has_special = input("Include special characters? (y/n): ")
if has_special == 'Y' or has_special == 'y':
    pwd_symbols.extend(special)
    #pwd_symbols = pywd_symbols + special

has_digits = input("Include digits? (y/n): ")
if has_digits == 'Y' or has_digits == 'y':
    pwd_symbols.extend(digits)
    #pwd_symbols = pwd_symbols + digits

new_password = "" #empty string to hold our new password

while len(new_password) != pwd_length:
    random_symbol = chr(random.choice(pwd_symbols)) #chr() converts the random interger to its encoded value in the ASCII
    new_password = new_password + random_symbol
#end of while loop

print(f"{new_password} has been generated.")