import os.path,pyAesCrypt
from os import path,remove

bufferSize = 64 * 1024
password = "andrej"

if os.path.exists("password_keeper.aes"):
    pass
else:
    pyAesCrypt.encryptFile("password_keeper.txt", "password_keeper.aes", password, bufferSize)
    if os.path.exists("password_keeper.txt"):
        remove("password_keeper.txt")
        print("File je enkriptovan.")



if os.path.exists("password_keeper.aes"):
    unos = "da"
    upit = input("Da li zelite da dekriptujete fajl? ")
    if upit == "da":
        pyAesCrypt.decryptFile("password_keeper.aes", "password_keeper.txt", password, bufferSize)
        remove("password_keeper.aes")
        print("File je dekriptovan.")
    else:
        print("File nije dekriptovan.")
