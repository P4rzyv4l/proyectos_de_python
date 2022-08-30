distncia = int(input("Ingrse la distancia recorrida en metros: "))
minutos = int(input("ingrese la cantidad de minutos: "))
segundos = int(input("ingrese la cantidad de segundos: "))
centecimas = int(input("ingrese la cantidad de centecimas: "))

tse=(minutos*60)+(centecimas/100)
vms=distncia/tse
vkm=(vms*3600)/1000

vkm = ((distncia/(minutos*60)+segundos+(centecimas/100)))*3600/1000

print ("la velocidad es de ",vkm," Km/h ")