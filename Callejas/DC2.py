import cv2
import numpy

def diferencia(MatrizA,MatrizB):
    (TamAX,TamAY, TamAZ) = MatrizA.shape
    for x in xrange(TamAX):
        for y in xrange(TamAY):
            (B1,G1,R1)=MatrizA[x,y]
            (B2,G2,R2)=MatrizB[x,y]

            if R1!=R2 or G1!=G2 or B1!=B2:
                print "Img1: ", (B1, G1, R1)
                print "Img2: ", (B2, G2, R2)
                print "Error en: ",(x,y)
                return False

    return True

ImagenA = cv2.imread("./image/LosV.jpg")
(Ax,Ay,Az) = ImagenA.shape
ImagenB = cv2.imread("./image/Carlos.jpg")
(Bx,By,Bz) = ImagenB.shape

ImagenC= cv2.imread("./image/Carlos.jpg")
(Cx,Cy,Cz) = ImagenB.shape
diff=cv2.absdiff(ImagenB, ImagenC)


num=[0,0,0]
BlackSection=numpy.full((Bx,By,Bz),num)

for x in xrange(Bx):
    for y in xrange(By):
        Muestra=ImagenB[x:(x+10),y:(y+10)]
        (TamMX,TamMY,TamMZ) = Muestra.shape
        cv2.imshow('Diferencias detectadas', Muestra)
        cv2.waitKey(0)
"""
        if TamMX == Bx and TamMY == By:
            DiferenciaAB = cv2.absdiff(ImagenB, Muestra)
            if diferencia(DiferenciaAB,diff)==True:
                cv2.imshow('Diferencias detectadas', Muestra)
                cv2.waitKey(0)
"""






