# -*- coding: utf-8 -*-
"""Password Generator | V1.0

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1M2JzKQNwFeGNSrmIEHzoVgIoYCZAhsrs

Logic:
*   Take user input on length of password
*   Requirements: Upper & lowercase, Numbers & Special Symbols
*   Save password to txt file
*   Print new password
"""

import random as rd
import string as st
from google.colab import drive
drive.mount('/content/drive/')

def password_generator(password_length):
  password_characters = st.ascii_letters + st.digits + st.punctuation
  password = ''.join(rd.choice(password_characters) for i in range(password_length))
  return password

# Main #
print("Welcome to Password Generator. All passwords will be as long as you want.")

password_length = int(input("\nHow many characters would you like to make your password? "))
user_password = password_generator(password_length)
with open('/content/drive/My Drive/Colab Notebooks/Credentials.txt', 'w') as output:
  output.write(f'Password: {user_password}')