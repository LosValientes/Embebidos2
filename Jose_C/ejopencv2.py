
import numpy as np
import cv2
from matplotlib import pyplot as plt

imagen = cv2.imread('./image/tux.jpeg')
cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
cv2.imshow("Original", imagen)
#print imagen.size

(x, y, z) = imagen.shape
print x, y, z

for j in xrange(y):
    for i in xrange(x):
        if (imagen[i,j][0] > 180):
            imagen[i,j] = (0, 255, 0)

cv2.namedWindow('New', cv2.WINDOW_NORMAL)
cv2.imshow('New', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()