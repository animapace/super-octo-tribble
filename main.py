# Calculadora de masa corporal

weight = float(input("Ingresa tu peso en libras: "))
height = float(input("Ingresa tu altura en metros: "))

weight = weight * (1/2.20462262)

mass = (weight / height ** 2 )

print(f"Tu masa corporal es: {mass}")