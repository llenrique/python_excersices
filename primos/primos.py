def is_primal(number):
    counter = 0
    for i in range(1, number + 1):
        if i == 1 or i == number:
            continue
        if number % i == 0:
            counter += 1
    if counter == 0:
        return True
    else:
        return False


def run():
    number = int(input('Escribe un número: '))
    if is_primal(number):
        print('Es primo')
    else:
        print('No es primo')


if __name__ == '__main__':
    run()