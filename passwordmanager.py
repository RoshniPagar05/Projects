import os
import random 
import string
passwords = {}
#load existing file
#aad update and delete password 
password_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"password.txt")
try:
    with open(password_file_path,"r") as file:
        for line in file:
            website,pwd = line.strip().split(":")
            passwords[website] = pwd
except:
    pass

def generte_password():
    chars = string.ascii_letters + string.digits + "!@#$%*&"
    password = "".join(random.choice(chars) for _ in range(8))
    return password
while True:
    print("-----Personal Password Manager-----")
    print("1.Save Password")
    print("2.view password")
    print("3.generate password")
    print("4.exit")

    choice = input("enter you choice:")
    if choice == "1":
        site = input("enter website : ")
        pwd = input("enter password: ")
        passwords[site] = pwd

        with open( password_file_path,"a") as file:
            file.write(f"{site}:{pwd}\n")
        print("saved")
    elif choice =="2":
        if not passwords:
            print("no data")
        else:
            for site,pwd in passwords.items():
                print(site,":",pwd)
    elif choice == "3":
        print("Generated password",generte_password())
    elif choice =="4":
        print("ok bye.....")
        break
    else:
        print("invalid input")
            