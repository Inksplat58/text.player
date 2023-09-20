import os
import time
while True:
    name = input('give me your name\n\n>')
    if name.isalpha():
        break
    else:
        print('please only use letters, try again')
