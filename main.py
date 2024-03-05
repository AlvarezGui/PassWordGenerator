import random
import string

def generate_password(leng):
    i = 0
    password = []
    while i != leng:
        char_or_num = random.randrange(1, 4)
        if char_or_num == 1:
            password.append(str(random.randrange(0, 10)))
        elif char_or_num == 2:
            password.append(random.choice(string.ascii_letters))
        else:
            password.append(random.choice(string.punctuation))
        i += 1

    password = ''. join(password)
    return password
leng_input = int(input("Leng: "))
print(generate_password(leng_input))
