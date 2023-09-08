import sys

if len(sys.argv) != 2:
    print(f"{sys.argv[0]} expected exactly one argument.")
    sys.exit(1)

password = sys.argv[1]
is_valid = False

# Do all the requirement checks here.

# print("!".islower())

lowercase = 0
uppercase = 0
number = 0
wierd_character = 0

for c in password:
    if c.islower() == True:
        lowercase += 1
    if c.isupper() == True:
        uppercase += 1
    if c.isnumeric() == True:
        number += 1
    if c in "$#@":
        wierd_character += 1

print(lowercase)
print(uppercase)
print(number)
print(wierd_character)

if (lowercase > 0 and uppercase > 0) == True:
    if (number > 0 and wierd_character > 0) == True:
        if 5 < len(password) < 17:
            is_valid = True
        else:
            is_valid = False

            
print(is_valid)
