#!/usr/bin/env python3
import random

PASSWORD_LENGTH = 16
NUM_TO_SELECT = 4

number_strings = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

lowercase_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                   'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

uppercase_alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                   'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*',
           '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', ':', ';', '"', "'", '<', '>', ',', '.', '?']

categories = [number_strings, lowercase_alpha, uppercase_alpha, symbols]
selected_chars = [random.sample(category, NUM_TO_SELECT)
                  for category in categories]

generated_password = []
for sublist in selected_chars:
    for char in sublist:
        generated_password.append(char)

random.shuffle(generated_password)


password_string = ''.join(generated_password)
print(password_string)
