import cv2
imagem = cv2.imread('china.jpg')
(b, g, r) = imagem[0, 0] #veja que a ordem BGR e não RGB
print('O pixel (0, 0) tem as seguintes cores:')
print('Vermelho:', r, 'Verde:', g, 'Azul:', b)
cv2.imshow("Nome da janela", imagem)
cv2.waitKey(0) #espera pressionar qualquer tecla