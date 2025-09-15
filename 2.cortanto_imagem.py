import cv2

imagem = cv2.imread('china.jpg')
recorte = imagem[200:450, 200:400]
cv2.imwrite("recorte.jpg", recorte) #salva no disco
cv2.imshow("Recorte da imagem", recorte)
cv2.imwrite("original.jpg", imagem)
cv2.waitKey(0)