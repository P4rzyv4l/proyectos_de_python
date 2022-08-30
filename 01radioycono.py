import math

import math

radio_cono=float(input("ingrese el radio del cono: "))
altura_cono=float(input("ingrese el altura del cono: "))
generatris_cono=float(input("ingrese el generatris del cono: "))

area_base = math.pi * radio_cono**2
area_lateral = math.pi * radio_cono * generatris_cono
are_total = area_base + area_lateral
volumen = (area_base * altura_cono)/3

print("")
print("el area de la base es: ",area_base)
print("El area lateral es:",area_lateral)
print("El area total es: ",are_total)
print("El volumen es ",volumen)

