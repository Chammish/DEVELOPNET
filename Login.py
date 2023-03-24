import random

user = ['rambo', 'beast', 'vimal', 'd2', 'ranjith', 'sundal']
lst = [502, 468, 958, 712, 584, 627]
username = input("Enter username: ")
password = input("Enter password: ")
key = 3
encrypt = []
for num in lst:
    encrypt1 = (num + key) % 10
    encrypt.append(encrypt1)
print(encrypt)
   
while(i<5):
    if username in user and int(password) in lst:
        print('Hi', username, 'you have been successfully logged in')
    else:
        print('Invalid username or password')
