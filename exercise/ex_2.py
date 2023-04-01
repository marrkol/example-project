import math
# kwadrat
a = 10

obwod = a * 4
pole = a * a

print("Obwód kwadratu wynosi: " + str(obwod) + ", a pole: " + str(pole) + ".")

# prostokąt
a = 10
b = 5

obwod = 2 * a + 2 * b
pole = a * b
print("Obwód prostokąta wynoi: " + str(obwod) + ", a pole:" + str(pole) + ".")

# koło, trapez, romb

# koło
r = 3
pi = math.pi

obwod = pi * 2 * r
pole = pi * r * r
print("Obwód koła wynosi: " + str(obwod) + ", a pole: " + str(pole) + ".")

#trapez
a=10
b=6
c=3
d=4
h=2

obwod=a+b+c+d
pole=0.5*(a+b)*h
print("Obwód trapezu wynosi: " + str(obwod) + ", a pole: " + str(pole) + ".")

# trojkat

a = 10
b = 20
c = 15
h = 12

obwod = a + b + c
pole = int((h * a) / 2)

print("Obwod trojkata wynosi " + str(obwod) + ", zas pole wynisi " + str(pole) + ".")

#romb

a = 5
h = 4

obwod= 4 * a
pole = a * h
print("Obwod rombu wynosi: " + str(obwod) + ",a pole: " + str(pole) + ".")


