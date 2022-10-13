from PyP100 import PyP100
import os
import json
import psutil

def main(ip, email, password):
    p100 = PyP100.P100(ip, email, password)
    p100.handshake()
    p100.login()

    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent
    print(battery)
    if plugged and percent > 80:
        p100.turnOff()
        print("Charging and more than 80%, TAPO OFF")
    elif not plugged and percent < 20:
        p100.turnOn()
        print("Not charging and less than 20%, TAPO ON")



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