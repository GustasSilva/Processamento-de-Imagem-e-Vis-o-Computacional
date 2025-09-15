import cv2
from matplotlib import pyplot as plt

img = cv2.imread('china.jpg')

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#converte P&B
cv2.imshow("Imagem P&B", img)
cv2.imwrite("way_pb.jpg", img)

#Função calcHist para calcular o hisograma da imagem
h = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.figure()
plt.title("Histograma P&B")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.plot(h)
plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)