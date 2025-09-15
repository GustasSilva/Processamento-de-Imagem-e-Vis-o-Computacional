import cv2

img = cv2.imread('china.jpg')
cv2.imshow("Original", img)

largura = img.shape[1]
altura = img.shape[0]
proporcao = float(altura/largura)
largura_nova = 320 #em pixels
altura_nova = int(largura_nova*proporcao)
tamanho_novo = (largura_nova, altura_nova)
img_redimensionada = cv2.resize(img, tamanho_novo, interpolation = cv2.INTER_AREA)

cv2.imshow('imagemRedimensionada', img_redimensionada)
cv2.waitKey(0)

#Redimensionamento pela metade

#img_redimensionada = img[::2,::2]
#cv2.imshow("Imagem redime", img_redim)
#cv2.imwrite("wayRedim.jpg", img_redim)
#cv2.waitKey(0)