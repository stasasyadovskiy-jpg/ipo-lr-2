import math
x = int(input("Введите x: "))
y = int(input("Введите y: "))
z = int(input("Введите z: "))
w = (math.fabs(math.cos(x) - math.cos(y)) ** (1 + 2 * (math.sin(y)**2))) * (1+z+(z**2/2)+(z**3)/3 + (z**4)/4) 
print(w)