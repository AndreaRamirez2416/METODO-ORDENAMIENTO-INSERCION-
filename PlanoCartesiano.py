import math
x1 = float(input("ingrese x1: "))
x2 = float(input("ingrese x2: "))
y1 = float(input("ingrese y1: "))
y2 = float(input("ingrese y2: "))
longitud = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
print("la distancia entre los dos puntos es:", longitud)
