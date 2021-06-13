def palindromo(palabra):
    palabra = palabra.replace(" ", "").lower()
    return palabra == palabra[::-1]

def run():
    palabra = input("Escribe una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo:
        print("Es un palindromo")
    else:
        print("No es palindromo")

if __name__ == '__main__':
    run()