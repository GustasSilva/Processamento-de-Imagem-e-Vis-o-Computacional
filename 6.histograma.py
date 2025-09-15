from matplotlib import pyplot as plt
import cv2


img = cv2.imread('china.jpg')

#histograma P&B
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# #converte P&B
# cv2.imshow("Imagem P&B", img)
# cv2.imwrite("way_pb.jpg", img)

# #Função calcHist para calcular o hisograma da imagem
# h = cv2.calcHist([img], [0], None, [256], [0, 256])
# plt.figure()
# plt.title("Histograma P&B")
# plt.xlabel("Intensidade")
# plt.ylabel("Qtde de Pixels")
# plt.plot(h)
# plt.xlim([0, 256])
# plt.show()
# cv2.waitKey(0)

#histograma colorido
cv2.imshow("Imagem Colorida", img)
#Separa os canais
canais = cv2.split(img)
cores = ("b", "g", "r")
plt.figure()
plt.title("'Histograma Colorido")
plt.xlabel("Intensidade")
plt.ylabel("Número de Pixels")
for (canal, cor) in zip(canais, cores):
    #Este loop executa 3 vezes, uma para cada canal
    hist = cv2.calcHist([canal], [0], None, [256], [0, 256])
    plt.plot(hist)
plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)