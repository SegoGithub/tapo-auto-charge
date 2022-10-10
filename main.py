from PyP100 import PyP100
import os
import json

def main(ip, email, password):
    print(ip, email, password)

# check if ./usercerds.json exists
if os.path.isfile("./usercreds.json"):
    print("Using existing usercreds.json")
    # load creds from file
    with open("./usercreds.json", "r") as f:
        usercreds = json.loads(f.read())
    # create PyP100 object
    main(usercreds["ip"], usercreds["email"], usercreds["password"])
else:
    print("First time? We need to get the credentials for your TP-Link account. (don't worry, it is stored locally and not sent anywhere 😃)")
    ip = input("Enter IP address of your Tapo: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    with open("usercreds.json", "w") as f:
        f.write("{\n")
        f.write(f'    "ip": "{ip}",\n')
        f.write(f'    "email": "{email}",\n')
        f.write(f'    "password": "{password}"\n')
        f.write("}")
    print("\033c", end="") # clear console
    main(ip, email, password)