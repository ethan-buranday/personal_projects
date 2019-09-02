"""
NOTE: THIS CHECKER IS STILL IN PROGRESS. ALGORITHIMS FOR COMPLEX NUMBERS NOT IMPLEMENTED YET.

"""
import re



user = PhoneChecker(
    input("Enter a phone number: "),
    input("Enter a message to identify the phone number(s): ")
)

# INPUTS
# phone_number = input("Enter a phone number: ")
# message = input("Enter a message to identify the phone number(s): ")
# area_code_phone_number = input("Enter a phone number to detect the area code: ")

class PhoneChecker:

    def __init__(self, phone_number, message):
        self.isPhoneNumber = phone_number
        self.isMessage = message

    
    # PHONE NUMBER CHECKER
    def isPhoneNumber(phone_number):
        """""""""
        Checks the format of the phone number.
        Scans the first three, second three, and last four digits and uses .isdecimal() function if the string contains decimals.
        Check hyphens in phone_number 3 and 7.
        """""""""
        if len(phone_number) != 12:
            return False
        for i in range (0, 3):
            if not phone_number[i].isdecimal():
                return False
        if phone_number[3] != '-':
            return False
        for i in range(4, 7):
            if not phone_number[i].isdecimal():
                return False
        if phone_number[7] != '-':
            return False
        for i in range(8, 12):
            if not phone_number[i].isdecimal():
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

    # # AREA CODE IDENTIFIER
    # """""""""
    # Identifies the area code for the phone number.
    # """""""""
    # def isAreaCode(area_code_phone_number):
    # area_code_phone_number = input("Enter a phone number to detect the area code: ")
    #     phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
    #     area_code = phoneNumRegex.search(area_code_phone_number)
        
        

PhoneChecker.






















# OUTPUT USING CLASS
# print(PhoneChecker.isPhoneNumber)
# print(PhoneChecker.isMessage)

# OUTPUTS
# """""""""""
# Prints the output
# """""""""""
# print(phone_number + ' is a phone number: ' + str(isPhoneNumber(phone_number)))
# print(isMessage(message))
# print(isAreaCode(area_code_phone_number.group()))

