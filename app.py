import random
value = input("Password length: ")
value2 = int(value)
keys = "#abcdefghijklmnopqrstuvwxyz123456!@#$%^98*?ASGDHFJKLNZBXVCQRWTYUIOP"
password = ""

for i in range(value2):
    password += random.choice(keys)

print(password)
