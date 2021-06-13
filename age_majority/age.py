print("Cual es tu nacionalidad?")
print("mxn: Mexicana")
print("usd: Americana")
nationality = input("")

age = int(input("Escribe tu edad: "))

AGE_MAJORITY = {
    "usd": 21,
    "mxn": 18   
}

age_majority = AGE_MAJORITY[nationality]
print(age_majority)

print(age_majority >= age)

if nationality == "mxn":
    if age >= age_majority:
        print("Usted es Mexican@ mayor de edad")
    else:
        print("Usted es Mexican@ menor de edad")
else:
    if age >= age_majority:
        print("Usted es American@ mayor de edad")
    else:
        print("Usted es American@ menor de edad")
