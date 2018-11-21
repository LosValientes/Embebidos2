import cv2
import numpy as np

imagen = cv2.imread("./image/tux.jpeg")
(x, y, z) = imagen.shape
cv2.imshow("Original", imagen)

for valy in xrange(y):
    for valx in xrange(x):
        if (imagen[valx, valy][0]>125 and imagen[valx, valy][1]>125 and imagen[valx, valy][2]>125):
            imagen[valx, valy] = [0,255,0]

cv2.imshow("cambio", imagen)
cv2.waitKey(0)