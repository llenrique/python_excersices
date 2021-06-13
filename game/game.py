from random import randrange

def guess_compare(guess, number):
    if number == guess:
        print('Ganaste!')
    elif number < guess:
        message = 'Selecciona un número mas grande: '
        number = int(input(message))
        guess_compare(guess, number)
    elif number > guess:
        message = 'Selecciona un número mas chico: '
        number = int(input(message))
        guess_compare(guess, number)


def run():
    max_range = 100
    guess = randrange(max_range)
    message = 'Selecciona un número entre 1 y {}: '.format(max_range)
    number = int(input(message))
    guess_compare(guess, number)


if __name__ == '__main__':
    run()