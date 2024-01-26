import random
print("----------PASSWORD GENERATOR---------")
print("Name: BANDARU SRIHITHA\n")


user = int(input("How many digits do you want in your password: "))

a2 = "1@#$%^&**"
a1 = "QWERTYUIOASDFGHJKLZXCVBNM"
a3 = "1234567890"
a4 = "qwertyuiopasdfghjklzxcvbnm"

comp = user - 3

password = ""

password += random.choice(a1)
password += random.choice(a2)
password += random.choice(a3)

for i in range(comp):
    password += random.choice(a4)

print(f"\n ------>Your generated password is: [{password}]")
