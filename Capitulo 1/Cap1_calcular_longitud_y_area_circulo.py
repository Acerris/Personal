import math

r = float(input("Valor del radio: "))

area= math.pi * r**2
Longitud = 2 * math.pi * r

#Para que solo salgan dos decimales colocamos el .2f
print(f"El area es: {area:.2f}")
print(f"La longitud del circulo es: {Longitud:.2f}")
