import cv2
import numpy as np

imagen = cv2.imread("./image/tux.jpeg",0)
recorte = cv2.imread("./image/recorte.jpeg",0)

cv2.imshow('Original', imagen)

w, h= recorte.shape[::-1]

efecto = cv2.TM_SQDIFF
res = cv2.matchTemplate(imagen,recorte,efecto)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

print(min_loc,max_loc,min_val,max_val)

limi = min_loc

contorno = (limi[0] + w, limi[1] + h)
cv2.rectangle(imagen, limi, contorno, 107, 2)

cv2.imshow('Encontrado', imagen)
cv2.imshow('Recorte', recorte)
cv2.imshow('Encontrado', imagen)
cv2.waitKey(0)