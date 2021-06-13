menu = """
Conversor de divisas

1.- De pesos colombianos a dolares
2.- De pesos argentinos a dolares
3.- De pesos mexicanos a dolares

Elige una opción: 
"""

choice = int(input(menu))

USD_EXCHANGE = {
    "mx": 19.74,
    "co": 3875,
    "ar": 65
}

def local_to_usd(amount, country):
    exchange = USD_EXCHANGE[country]
    float_usd = amount / exchange
    return float_to_str(float_usd)

def float_to_str(float_usd):
    float_usd = round(float_usd, 2)
    return str(float_usd)

if choice == 1:
    amount = float(input("Cuantos pesos colombianos tienes?: "))
    usd = local_to_usd(amount, "co")
    print("Tienes $" + usd + " dolares")
elif choice == 2:
    amount = float(input("Cuantos pesos argentinos tienes?: "))
    usd = local_to_usd(amount, "ar")
    print("Tienes $" + usd + " dolares")
elif choice == 3:
    amount = float(input("Cuantos pesos mexianos tienes?: "))
    usd = local_to_usd(amount, "mx")
    print("Tienes $" + usd + " dolares")
else:
    print("Selecciona una opción valida")
