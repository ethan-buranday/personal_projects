
import re

# INPUTS
text = input("Enter a phone number: ")
message = input("Enter a message to identify the phone number(s): ")


# PHONE NUMBER CHECKER
def isPhoneNumber(text):
    """"""""""
    Checks the format of the phone number.
    Scans the first three, second three, and last four digits and uses .isdecimal() function if the string contains decimals.
    Check hyphens in text 3 and 7.
    """""""""
    if len(text) != 12:
        return False
    for i in range (0, 3):
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

# MESSAGE SCANNER
def isMessage(message):
    """""""""""
    Detects any phone number(s) that are in the message.
    """""""""""
    for i in range(len(message)):
        chunk = message[i:i+12]
        if isPhoneNumber(chunk):
            return("Phone number(s) found: " + str(chunk))
        else:
            return("No phone number(s) detected.")


# OUTPUTS
    """""""""""
    Prints the output
    """""""""""
print(text + ' is a phone number: ' + str(isPhoneNumber(text)))
print(isMessage(message))