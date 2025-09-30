import math
a = int(input("Введите длину основы трапеции: "))
b = int(input("И вторую тоже: "))
c = int(input("Введите длину боковой стороны трапеции: "))
d = int(input("И вторую тоже: "))
p = (a+b+c+d) / 2
S = ((a+b) / math.fabs(a-b)) * (math.sqrt((p-a)*(p-b)*(p-a-c)*(p-a-d)))  
print(S)