precio = float(input("¿Cual es el precio de el proucto?: "))
pago = float(input("¿Con cualto dinero pagara?: "))

cambio = precio - pago
faltante = pago - precio

if (cambio<0):
    print("Pago insuficiente. Falta la cantidad de ",faltante)

elif(cambio==0):
    print("El pago es exacto. No hay cambio")

if (cambio>0):
    print("El cambio es: ",cambio)