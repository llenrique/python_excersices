import random
from string import punctuation, ascii_uppercase, ascii_lowercase, digits

def password_generator(pass_length):
    chars = ascii_uppercase + ascii_lowercase + digits + punctuation
    password = ''

    for i in range(pass_length):
        password += random.choice(chars)

    return password


def run():
    pass_length = int(input('Cuantos caracteres quieres en tu contraseña: '))
    password = password_generator(pass_length)
    print(password)


if __name__ == '__main__':
    run()