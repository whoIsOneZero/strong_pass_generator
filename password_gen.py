#!/usr/bin/env python3
import random

PASSWORD_LENGTH = 16
num_to_select = 4

number_strings = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

lowercase_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                   'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

uppercase_alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                   'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*',
           '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', ':', ';', '"', "'", '<', '>', ',', '.', '?']

rand_1 = random.sample(number_strings, num_to_select)
rand_2 = random.sample(lowercase_alpha, num_to_select)
rand_3 = random.sample(uppercase_alpha, num_to_select)
rand_4 = random.sample(symbols, num_to_select)

char_lists = [rand_1, rand_2, rand_3, rand_4]

generated_password = []

while len(generated_password) < 16:
    random_list = random.choice(char_lists)

    random_item = random.choice(random_list)

    generated_password.append(random_item)


password_string = ''.join(generated_password)
print(password_string)
