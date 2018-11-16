import cv2
import numpy


image = cv2.imread("./image/tux.jpeg")
cv2.imshow("Original",image)

(x,y,z)=image.shape

for a in xrange(x):
    for b in xrange(y):
        (B, G, R) = image[a,b]
        if B>30 and G>30 and R>30:
            if (R-G)<0:
                RES=G-R
            else:
                RES=R-G

            if (R-B)<0:
                RES1=B-R
            else:
                RES1=R-B

            if (G-B)<0:
                RES2=B-G
            else:
                RES2=G-B

            if RES<=30 or RES1<=30 or RES2<=30:
                image[a,b] = (0,255,0)
        if R>220 and G>220 and B>220:
            image[a, b] = (0, 255, 0)
        if R > 240 and G > 180 and B > 90:
            image[a, b] = (0, 255, 0)



cv2.imshow("Cambiado",image)
#plantilla =  numpy.zeros(image.shape[:2],dtype)

cv2.waitKey(0)
