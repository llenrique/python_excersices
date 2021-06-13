def run():
    LIMITE = 1000
    counter = 0
    power_2 = 2**counter

    while power_2 < LIMITE:
        print('2 elevado a ' + str(counter) + ' es igual a ' + str(power_2))
        counter += 1
        power_2 = 2**counter

if __name__ == '__main__':
    run()