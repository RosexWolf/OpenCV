#librerias
import cv2
from cv2 import imshow
import numpy as np

imgText = "Color"

#lectura de imagen
img = cv2.imread("imagen 1.jpg")
img2 = cv2.imread("imagen 2.jpg")
img3 = cv2.imread("imagen 3.jpg")

imgB = cv2.imread("imagen 1.jpg",cv2.IMREAD_GRAYSCALE)
imgB2 = cv2.imread("imagen 2.jpg",cv2.IMREAD_GRAYSCALE)
imgB3 = cv2.imread("imagen 3.jpg",cv2.IMREAD_GRAYSCALE)

Hori = np.concatenate((img,img2,img3),axis=1)
Hori2 = np.concatenate((imgB,imgB2,imgB3),axis=1)

imshow("Imaagen a Color",Hori)
imshow("imagen a escala de grises",Hori2)

cv2.waitKey(0)
cv2.destroyAllWindows() 
