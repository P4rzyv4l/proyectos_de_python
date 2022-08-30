x1 = float(input(" Ingrese la coordenada en 'X' del punto 1: "))
y1 = float(input(" Ingrese la coordenada en 'Y' del punto 1: "))

x2 = float(input(" Ingrese la coordenada en 'X' del punto 2: "))
y2 = float(input(" Ingrese la coordenada en 'Y' del punto 2: "))

x3 = float(input(" Ingrese la coordenada en 'X' del punto 3: "))
y3 = float(input(" Ingrese la coordenada en 'Y' del punto 3: "))

area_triangulo = 1/2 * abs (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

print("El area del triangulo es: ", area_triangulo)