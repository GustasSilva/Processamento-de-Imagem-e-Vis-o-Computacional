import cv2

img = cv2.imread('china.jpg')
cv2.imshow("Original", img)

flip_hor = img[:,::-1] #comando equivalente abaixo
#flip_horizontal = cv2.flip(img, 1)
cv2.imwrite("way_flip_hor.jpg", flip_hor)
cv2.imshow("Flip Horizontal", flip_hor)

flip_vertical = img[::-1,:] #comando equivalente abaixo
#flip_vertical = cv2.flip(img, 0)
cv2.imshow("Flip Vertical", flip_vertical)
cv2.imwrite("way_flip_vert.jpg", flip_vertical)

flip_hv = img[::-1,::-1] #comando equivalente abaixo
#flip_hv = cv2.flip(img, -1)
cv2.imshow("Flip Horizontal e Vertical", flip_hv)
cv2.imwrite("way_flip_hv.jpg", flip_hv)

cv2.waitKey(0)