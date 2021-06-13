def palindromo(palabra):
    palabra = palabra.replace(" ", "").lower()
    return palabra == palabra[::-1]

def run():
    palabra = input("Escribe una palabra: ")
    if palindromo(palabra):
        print("Es un palindromo")
    else:
        print("No es palindromo")

if __name__ == '__main__':
    run()
