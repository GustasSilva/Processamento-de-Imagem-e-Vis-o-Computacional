import cv2

imagem = cv2.imread('china.jpg')

altura, largura = imagem.shape[:2]
print(f"Dimensões da imagem: {largura}x{altura}")

xInicial = 20
yInicial = 20
xFinal = 180
yFinal =  80

recorte = imagem[yInicial:yFinal, xInicial:xFinal]  # fatia da imagem
negativo = 255 - recorte  # aplica negativo
imagem[yInicial:yFinal, xInicial:xFinal] = negativo 

cv2.imshow("Imagem com negativo aplicado", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()