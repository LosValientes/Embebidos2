import cv2
import numpy as np

Imagen = cv2.imread("./image/LosV.jpg")
(cx,cy,cz)=Imagen.shape

Carlos = cv2.imread("./image/Carlos.jpg")
Copito = cv2.imread("./image/Copito.jpg")
Marcelo = cv2.imread("./image/Marcelo.jpg")
Mario = cv2.imread("./image/Mario.jpg")
Turco = cv2.imread("./image/Turco.jpg")
Yimmi = cv2.imread("./image/Yimmi.jpg")

def busqueda(section, name):
    (x,y,z)= section.shape
    respuesta = cv2.matchTemplate(Imagen, section, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(respuesta)
    print max_val,min_val
    cv2.rectangle(Imagen, max_loc, (max_loc[0] + x - 5, max_loc[1] + y), (0, 0, 0), 1)
    cv2.imshow('umbral', Imagen)
    cv2.waitKey(0)


busqueda(Carlos, "Carlos")
busqueda(Copito, "Copito")
busqueda(Mario, "Mario")
busqueda(Marcelo, "Marcelo")
busqueda(Turco, "Turco")
busqueda(Yimmi, "Yimmi")
