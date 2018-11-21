import cv2
import numpy as np

#Abre imagen
image = cv2.imread("./image/LosV.jpg")
cv2.imshow('Imagen_Foto', image)
#Abre fragmento
frag = cv2.imread("./image/Yimy.jpg")
cv2.imshow('Cara', frag)
w, h, e = frag.shape

#Compara
c = cv2.matchTemplate(image, frag, cv2.TM_CCOEFF_NORMED)

# precision
p = 0.99

loc = np.where(c >= p)
l2 = zip (*loc[::-1]) # Organizo la listas
print l2
for i in (l2):
    cv2.rectangle(image, i, (i[0] + w, i[1] + h), (0, 255, 255))

cv2.imshow('Aqui esta', image)
cv2.waitKey(0)