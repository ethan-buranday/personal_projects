#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
NOTE: THIS CHECKER IS STILL IN PROGRESS. ALGORITHIMS FOR COMPLEX NUMBERS NOT IMPLEMENTED YET.

"""
import time
import sys
import re




# STARTUP
def main():
    print(""" 

        ██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗    ████████╗ ██████╗     ██████╗ ██╗  ██╗ ██████╗ ███╗   ██╗███████╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
        ██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝    ╚══██╔══╝██╔═══██╗    ██╔══██╗██║  ██║██╔═══██╗████╗  ██║██╔════╝    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
        ██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗         ██║   ██║   ██║    ██████╔╝███████║██║   ██║██╔██╗ ██║█████╗      ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
        ██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝         ██║   ██║   ██║    ██╔═══╝ ██╔══██║██║   ██║██║╚██╗██║██╔══╝      ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
        ╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗       ██║   ╚██████╔╝    ██║     ██║  ██║╚██████╔╝██║ ╚████║███████╗    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
         ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝       ╚═╝    ╚═════╝     ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝                                                                                                                                                                                                
    """)

    time.sleep(2)

    print("""
    NOTE: THIS PROGRAM IS A WORK IN PROGRESS! SOME PHONE NUMBERS MIGHT NOT WORK. I AM CURRENTLY WORKING ON ADDING EXTENSION NUMBERS AND OTHER STUFFS. PLEASE CONTACT ME FOR
          SUGGESTIONS AT BURANDAY.ETHAN@GMAIL.COM OR THROUGH GITHUB.
    """)


def continue_to_program():
    proceed = input("""
        WOULD YOU LIKE TO PROCEED?
        1: YES
        2: NO
        
        ENTER CHOICE HERE: """)

    if proceed == "1":
        menu()
    elif proceed == "2":
        print("""












        
        EXISTING THE PROGRAM
        
        










        """)
        time.sleep(1)
        quit()
    elif proceed == "" or proceed == " ":
        print("""
        
        
        TRY AGAIN!
        
        
        """)
        continue_to_program()








# MENU
def menu():
    choice = input("""

        WELCOME TO PHONE CHECKER")
        Please select the following choices below: 
        1: PHONE CHECKER
        2: MESSAGE SCANNER
        3: AREA CODE DETECTOR

        ENTER CHOICE HERE: """)

    if choice == "1":
        isPhoneNumber()
    elif choice == "2":
        isMessage()

    elif choice == "3":
        menu()
        #isAreaCode()

    elif choice == "" or choice == " ":
        print("""
        
        CHOICE NOT VALID, PLEASE ENTER VALID CHOICE!
        
        """)
        menu()
    else:
        print("""
        
        CHOICE NOT VALID, PLEASE ENTER VALID CHOICE!
        
        """)


# PHONE NUMBER CHECKER
def isPhoneNumber():
    # """""""""
    # Checks the format of the phone number.
    # Scans the first three, second three, and last four digits and uses .isdecimal() function elif the string contains decimals.
    # Check hyphens in phone_number 3 and 7.
    # """""""""

    print("""
    
    
    _______  ____  ____   ___   ____  _____  ________     ______  ____  ____  ________    ______  ___  ____   ________  _______     
   |_   __ \|_   ||   _|.'   `.|_   \|_   _||_   __  |  .' ___  ||_   ||   _||_   __  | .' ___  ||_  ||_  _| |_   __  ||_   __ \    
     | |__) | | |__| | /  .-.  \ |   \ | |    | |_ \_| / .'   \_|  | |__| |    | |_ \_|/ .'   \_|  | |_/ /     | |_ \_|  | |__) |   
     |  ___/  |  __  | | |   | | | |\ \| |    |  _| _  | |         |  __  |    |  _| _ | |         |  __'.     |  _| _   |  __ /    
    _| |_    _| |  | |_\  `-'  /_| |_\   |_  _| |__/ | \ `.___.'\ _| |  | |_  _| |__/ |\ `.___.'\ _| |  \ \_  _| |__/ | _| |  \ \_  
   |_____|  |____||____|`.___.'|_____|\____||________|  `.____ .'|____||____||________| `.____ .'|____||____||________||____| |___|
    
    
    """)

    phone_number = input("""
    
        Enter a phone number: """)

    """
    REWORK ON PHONE NUMBER AND ADD REGEX INSTEAD OF IF STATEMENTS
    """

    # PHONE VALIDATOR USING REGEX
    phone_number_regex = re.compile('\d{3}-\d{3}-\d{4}')
    if re.match(phone_number_regex, phone_number):
        print("""
        
        
        VALID PHONE NUMBER
        
        
        """)
        menu()
    else:
        print("""
        
        
        NOT VALID PHONE NUMBER
        
        
        """)
        menu()

    # OLD PHONE SCANNER
    # if len(phone_number) != 12:
    #     return False
    # for i in range (0, 3):
    #     if not phone_number[i].isdecimal():
    #         return False
    # if phone_number[3] != '-':
    #     return False
    # for i in range(4, 7):
    #     if not phone_number[i].isdecimal():
    #         return False
    # if phone_number[7] != '-':
    #     return False
    # for i in range(8, 12):
    #     if not phone_number[i].isdecimal():
    #         return False
    # return True


# MESSAGE SCANNER
def isMessage():
    """""""""""
     Detects any phone number(s) that are in the message.
    """""""""""

    message = input("Enter a message to identify the phone number(s): ")
    phone_number_regex = re.compile('\d{3}-\d{3}-\d{4}')
    if re.Pattern(phone_number_regex, message):
        print("Phone number(s) found: " + phone_number_regex)
    else:
        print("No phone number(s) found.")


    # message = input("Enter a message to identify the phone number(s): ")
    # phone_number_regex = re.findall('\d{3}-\d{3}-\d{4}', message)
    # for phone_number in phone_number_regex:
    #     print("Phone number(s) found: " + phone_number)
    # else:
    #     print("No phone number(s) found.")



# print("Phone number(s) found: " + phone_number)
# print("No phone number(s) found.")



        # chunk = message[i:i+12]
        # if isPhoneNumber(chunk):
        #     return "Phone number(s) found: " + str(chunk)
        # else:
        #     return "No phone number(s) detected."



    # message = input("Enter a message to identify the phone number(s): ")
    # for i in range(len(message)):
    #
    #     chunk = message[i:i + 12]
    #     if isPhoneNumber(chunk):
    #         return ("Phone number(s) found: " + str(chunk))
    #     else:
    #         return ("No phone number(s) detected.")


# # AREA CODE IDENTIFIER
# def isAreaCode():
#     area_code = input("Enter a phone number to detect the area code: ")
#     phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
#     area_code = phoneNumRegex.search(area_code)
#     return "Area code detected: " + area_code.group(1)


# OUTPUTS
# """""""""""
# Prints the output
# """""""""""
# print(phone_number + ' is a phone number: ' + str(isPhoneNumber(phone_number)))
# print(isMessage(message))
# print(isAreaCode(area_code))




main()
continue_to_program()
# isPhoneNumber()
