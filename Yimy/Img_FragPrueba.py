import cv2
import numpy

image = cv2.imread("./image/LosV.jpg")
frag = cv2.imread("./image/Turco.jpg")
cv2.imshow('Imagen_Foto', image)
cv2.imshow('Cara', frag)
lista = []
posx = []
posy = []

(Ix, Iy, P1) = image.shape
(Fx, Fy, P2) = frag.shape
print(Fx,Fy,P2)
for x in xrange(Ix):
    for y in xrange(Iy):
        Aux = image[x:(x + Fx), y:(y + Fy)]
        (Ax, Ay, P3) = Aux.shape
        if Ax == Fx and Ay == Fy:
            Diferencia = cv2.absdiff(Aux, frag)
            lista.append(Diferencia.max())
            posx.append(x)
            posy.append(y)
menor = min(lista)
print(menor)
for i in xrange(len(lista)):
    if menor == lista[i]:
        cv2.rectangle(image, (posy[i], posx[i]), (posy[i] + Fy, posx[i]+ Fx), (0, 255, 255))
        cv2.imshow('Aqui esta', image)
        cv2.waitKey(0)

