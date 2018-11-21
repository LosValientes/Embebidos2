import cv2
import numpy

Imagen = cv2.imread("./image/LosV.jpg")
Carlos = cv2.imread("./image/Carlos.jpg")
Copito = cv2.imread("./image/Copito.jpg")
Marcelo = cv2.imread("./image/Marcelo.jpg")
Mario = cv2.imread("./image/Mario.jpg")
Turco = cv2.imread("./image/Turco.jpg")
Yimmi = cv2.imread("./image/Yimmi.jpg")

def buscar(Matriz1,Matriz2):
    (Ax, Ay, Az) = Matriz1.shape
    (Bx, By, Bz) = Matriz2.shape
    for x in xrange(Ax):
        for y in xrange(Ay):
            Muestra = Matriz1[x:(x + Bx), y:(y + By)]
            (TamMX, TamMY, TamMZ) = Muestra.shape

            if TamMX == Bx and TamMY == By:
                Diferencia = cv2.absdiff(Muestra, Matriz2)
                if Diferencia.max() < 20:
                    cv2.rectangle(Matriz1, (y, x), (y + By, x + Bx), (0, 0, 0), 1)
                    cv2.imshow('Encontrado', Matriz1)
                    cv2.waitKey(0)

buscar(Imagen,Carlos)
buscar(Imagen,Copito)
buscar(Imagen,Mario)
buscar(Imagen,Marcelo)
buscar(Imagen,Turco)
buscar(Imagen,Yimmi)









