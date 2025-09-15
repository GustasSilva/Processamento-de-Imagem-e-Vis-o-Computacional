import cv2

image1 = cv2.imread('cavalo.jpg')
image2 = cv2.imread('india.jpg')
imageAdd = cv2.addWeighted(image1, 0.5, image2, 0.4, 0)
cv2.imshow('Adição de Imagens', imageAdd)
cv2.imwrite("img1=image2.jpg", imageAdd)
cv2.waitKey(0)