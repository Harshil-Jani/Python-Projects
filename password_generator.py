import random
import time

print('Generate Passwords : ')
number = int(input("Enter the number of Passwords : "))
chars = 'abcdefghijklmnopqrttuvwxyzABCDEFGHIJKLMNOPQRTUVWXYZ!@#$%^&*0123456789'
length = int(input('Enter the length of Passwords : '))

print("Your Password Suggestions are : ")
time.sleep(2)
for pwd in range(number):
    for c in range(length):
        a = random.choice(chars)
        print(a,end="")
    time.sleep(1)
    print()