import random
import string

def generate_password(m):
    password = ''
    for i in range(m):
        while True:
            c = random.choice(string.ascii_letters + string.digits)
            if c not in 'lIoO01':
                password += c
                break
    return password

def main(n, m):
    passwords = set()
    while len(passwords) < n:
        password = generate_password(m)
        passwords.add(password)
    return list(passwords)
passwords = main(9, 10)
print(passwords)
