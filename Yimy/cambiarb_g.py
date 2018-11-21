import cv2

image = cv2.imread("./image/tux.jpeg")
#image = cv2.imread("home/yimy/imagen2.jpg")
cv2.imshow("ventana1", image)

(X,Y,P) = image.shape
print Y,X,P

for i in xrange(X):
   for j in xrange(Y):
       (B, G, R) = image[i,j]
       if (B>=30 and G>=30 and R>=30):
           if (B >= G):
              G1 = B - G
           else:
              G1 = G - B
           if (B >= R):
              G2= B - R
           else:
              G2 = R - B
           if (R >= G):
              G3 = R - G
           else:
              G3 = G - R
           if (G1 <= 50 and G2 <= 50 and G3 <= 50):
              image[i, j] = (0, 255, 0)

cv2.imshow("ventana2", image)
cv2.waitKey(0)
