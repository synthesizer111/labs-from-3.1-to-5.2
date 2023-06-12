import random

passwords = []
password_length = 8
num_passwords = 5

while len(passwords) < num_passwords:
    curr_password = ''
    while len(curr_password) < password_length:
        char = chr(random.randint(33, 126))
        curr_password += char
        if len(set(curr_password)) < len(curr_password):
            curr_password = curr_password[:-1]
    passwords.append(curr_password)

print(passwords)