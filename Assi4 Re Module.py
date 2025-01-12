import re

def validate_name():
    while True:
        name = input("Enter your Name: ")
        # Regular expression to allow alphabets, spaces, dots, and apostrophes
        if re.match(r"^[A-Za-z\s\.'']+$", name):
            print(f"Valid Name: {name}")  # Print the valid name
            return name
        else:
           return False

def validate_aadhaar():
    while True:
        aadhaar = input("Enter Aadhaar number (12 digits): ")
        if len(aadhaar) != 12:
            print("Aadhaar must contain exactly 12 digits.")
        elif re.match(r"[0-9]{12}", aadhaar):
            print(f"Valid Aadhaar number: {aadhaar}")  # Print the valid Aadhaar number
            return aadhaar
        else:
            return False
           

def validate_pan():
    while True:
        pan = input("Enter PAN number (e.g., ABCDE1234F): ")
        if re.match(r"^[A-Z]{5}[0-9]{4}[A-Z]{1}$", pan):
            print(f"Valid PAN number: {pan}")  # Print the valid PAN number
            return pan
        else:
            return False

def validate_phone():
    while True:
        phone = input("Enter Phone number (10 digits): ")
        if re.match(r"^[789][0-9]{9}$", phone):
            print(f"Valid Phone number: {phone}")  # Print the valid phone number
            return phone
        else:
            return False

# Calling the functions and storing the validated information
name = validate_name()
aadhaar = validate_aadhaar()
pan = validate_pan()
phone = validate_phone()

# Display the validated information
print("\nThe entered details are:")
print("Name:", name)
print("Aadhaar Number:", aadhaar)
print("PAN Number:", pan)
print("Phone Number:", phone)
