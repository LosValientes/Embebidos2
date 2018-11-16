import numpy
import cv2
image = cv2.imread('./image/tux.jpeg')
(x,y,z) = image.shape

for i in xrange(x):
    for j in xrange(y):
        (B, G, R) = image[i,j]
        if (B > 30) and (G > 30) and (R > 30):
            if (B-G) < 0:
                g1 = G-B
            else:
                g1 = B-G

            if (G-R) < 0:
                g2 = R-G
            else:
                g2 = G-R

            if (R-B) < 0:
                g3 = B-R
            else:
                g3 = R-B

#            if numpy.array_equal(image[i, j], (255, 255, 255)):
#                image[i,j] = (0, 255, 0)
            if (g1 <= 50) or (g2 <= 50) or (g3 <= 50):
                image[i,j] = (0, 255, 0)

cv2.imshow("Tux Verde", image)
cv2.waitKey(0)