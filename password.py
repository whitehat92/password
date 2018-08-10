from random import choice
import sys


chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_-#$%&/()=?@*{}[]1234567890"
r = input("How many characters do you want?: ")
password = ""
print("you selected" + " " + r + " " + "chars.")
if int(r) <= 8:
    print("Not possible to generate password. Please choose a higher number");
elif int(r) >= 8:
    print ("Generating password...")
    print(password.join(choice(chars) for i in range(int(r))))


