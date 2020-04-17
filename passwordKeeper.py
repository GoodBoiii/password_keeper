#Andrej Plavsic 17.04.2020

import os.path,pyAesCrypt
from os import path,remove

"""
#FILE ENCRYPTION
def encrypt_file():
    try:
        pyAesCrypt.encryptFile("password_keeper.txt", "password_keeper.aes", password, bufferSize)
        if os.path.exists("password_keeper.txt"):
            file.close()
            remove("password_keeper.txt")
            print("File je enkriptovan.")   

    except PermissionError:
        print("File je u procesu.")

#FILE DECRYPTION
def decrypt_file():
    try:
        pitanje = input("Da li zelis da dekriptujes fajl? ")
        if pitanje == "da" or "DA":
            pyAesCrypt.decryptFile("password_keeper.aes", "password_keeper.txt", password, bufferSize)
            remove("password_keeper.aes")
            print("File je dekriptovan.")

        else:
            print("File ce ostat enkriptovan.")
    except:
        print("File je u procesu.")

"""

bufferSize = 64 * 1024


if path.exists("password_keeper.txt") == False:
    file = open("password_keeper.txt","a")
    print("File has been created.")
else:
    print("File already exists.")



password = input("Unesi master sifru: ")
if password == "andrej":
    unos = int(input("Unesi koliko naloga dodajes: "))
    for i in range(unos):
        for j in range(1):
            gmail = input("Unesi ime svog naloga: ")
            password = input("Unesi naziv naloga za password: ")
            email_input = input("Unesi svoj email: ")
            password_input = input("Unesi svoju sifru: ")

        recnik = {
            gmail:email_input,
            password:password_input
        }

        #write to file
        def write_file():
            file = open("password_keeper.txt","a")
            file.write(str(recnik)+"\n")
            file.close()
            
        write_file()

else:
    exit("Nisi admin!")


