import cv2
import numpy as np

# membaca file gambar kucing yang berada dalam  folder
image = cv2.imread("semangka.png")
print('Image', image)

# menampilkan citra original
cv2.imshow("Gambar Semangka Original", image)

# menampilkan citra grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale", gray)

# menampilkan citra hsv
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV Picture", hsv)

img_median = cv2.medianBlur(hsv, 5)
cv2.imshow('Median Filter 0', img_median)

img = img_median[:,:,1]
th, img = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
cv2.imshow("Otsu Tresholding", th)

kernel = np.ones((7,7), np.uint8)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imshow('Opening', opening)

dest_and = cv2.bitwise_and(image,image,mask = opening)
cv2.imshow('Bitwise And', dest_and)

cv2.waitKey(0)
cv2.destroyAllWindows()
