import winreg
import socket
import smtplib

def get_serial_number():
    # Open the registry key where the serial number is stored
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion")

    # Read the value of the 'ProductID' key to retrieve the serial number
    serial_number = winreg.QueryValueEx(key, "ProductID")[0]

    # Close the registry key
    winreg.CloseKey(key)

    return serial_number

def send_email(email_address, password, serial_number):
    # Set up the SMTP server and login to it
    smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
    smtp_server.starttls()
    smtp_server.login(email_address, password)

    # Construct the message body
    message = "Serial number: {}".format(serial_number)

    # Send the email
    smtp_server.sendmail(email_address, email_address, message)

    # Shut down the SMTP server
    smtp_server.quit()

# Retrieve the serial number
serial_number = get_serial_number()

# Get the email address and password to send the email from
email_address = input("Enter your email address: ")
password = input("Enter your email password: ")

# Send the email with the serial number
send_email(email_address, password, serial_number)
