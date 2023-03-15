
# name = input("Enter your full name: ")
#phone_number = input("Enter your phone number: ")



# result = len(name)
#   len determines the length of the name input, including spaces

# result = name.find("o")
#   .find looks for the specified character in the input. Index starts at 0

# result = name.rfind("o")
#   .rfind starts from the end of the end of the input and goes backwards

# name = name.capitalize()
#   .capitalize will capitalize the first letter of the given input

# name = name.upper()
#   .upper will capitalize all the characters of the input

# name = name.lower()
#   .lower will lower case any of the input characters

# result = name.isdigit()
#   .isdigit will return false if the entire input is not numbers. Is boolean (T/F) by nature

# result = name.isalpha()
#   .isalpha will return false if the entire input is not alphabetical characters. Spaces count as non-alpha,
#   boolean in nature

#result = phone_number.count("-")
#   .count will count the number of specified characters in a given input

#phone_number = phone_number.replace("-", " ")



#print(phone_number)





# Validate user input
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits


username = input("Enter your desired username: ")



if len(username) > 12:
    print("Error: Username longer than 12 characters.")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces.")
elif not username.isalpha():
    print("Your username can't contain numbers.")
else:
    print(f"Welcome {username}")




























