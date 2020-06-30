def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
        if text[3] != '-':
            return False
        for i in range(4, 7):
            if not text[i].isdecimal():
                return False
            if text[7] != '-':
                return False
            for i in range(8, 12):
                if not text[i].isdecimal():
                    return False
                return True

print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))
print('Moshi moshi is a phone number:')
print(isPhoneNumber('Moshi moshi'))

#this is smart - for every letter in a string, they look at the next 12
#letters to form a string, then they look to see whether this string is a 
#phone number.
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
        print('Done')

#regular expressions are called regexes for short
#examples of regexes are \d which refers to a digit character
#\n as a new line \p as a new paragraph \t or 09x as a tab etc
#
print('red\n')
print(r'red\n')