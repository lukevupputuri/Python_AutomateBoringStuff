
import re, pyperclip


# Create a regex object for phone numbers

phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
(
((\d\d\d)| (\(\d\d\d\)))?     # area code (optional)
(\s|-)                       # first seperator
\d\d\d                       # first 3 digits
-                            # seperator
\d\d\d\d                     # last 4 digits
(((ext(\.)?\s)|x)            #extension word part

(\d{2,5}))?                  # extension number part
)
''', re.VERBOSE)

# Create a regex object for email addresses
           
emailRegex = re.compile(r'''

[a-zA-Z0-9_.+]+                    # name part - character class
 @                   # @symbol
[a-zA-Z0-9_.+]+                   # domain name part


''', re.VERBOSE)

#Get the text off the clipboard

text = pyperclip.paste()


# TODO: Extract the email/phone from this text

extractedPhone = phoneRegex.findall(text)


# TODO: Copy the extracted email/phone to the clipboard


extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []

for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])
    

results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)

pyperclip.copy(results)

 




