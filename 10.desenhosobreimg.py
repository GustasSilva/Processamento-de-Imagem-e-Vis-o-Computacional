import cv2

imagem = cv2.imread('img1=image2.jpg')
vermelho = (0, 0, 255)
verde = (0, 255, 0)
azul = (255, 0, 0)
cv2.rectangle(imagem, (300, 300), (120, 120), azul, 10)
for raio in range(0, 100, 50):
    cv2.circle(imagem, (350, 100), raio, vermelho)

cv2.imshow("Desenhando sobre a imagem", imagem)
cv2.waitKey(0)