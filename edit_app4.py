import cv2
import numpy as np

image = cv2.imread('hello.jpg')

#ret, mask = cv2.threshold(img[:, :,2], 200, 255, cv2.THRESH_BINARY)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower_red = np.array([110,50,50])
upper_red = np.array([130,255,255])

mask = cv2.inRange(hsv, lower_red, upper_red)

mask3 = np.zeros_like(image)
mask3[:, :, 0] = mask
mask3[:, :, 1] = mask
mask3[:, :, 2] = mask

blue = cv2.bitwise_and(image, mask3)
red = cv2.cvtColor(blue, cv2.COLOR_BGR2RGB)
b, g, r = cv2.split(red)
green = cv2.merge([g, r, b])


#green=[[[0,0,255%j] for j in i] for i in blue]
#green=np.array(green)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
img  = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

gray = cv2.bitwise_and(img, 255 - mask3)



bluefinal = gray + blue
redfinal = gray + red
greenfinal = gray + green

cv2.imshow('blue', blue)
cv2.imshow('gray', gray)
cv2.imwrite("bluefinal.jpg", bluefinal)
cv2.imshow("mask", mask)
cv2.imshow("mask3", mask3)
cv2.imshow("image", image)
cv2.imshow("red",red)
cv2.imwrite("redfinal.jpg",redfinal)
cv2.imshow("green",green)
cv2.imwrite("greenfinal.jpg",greenfinal)


import imageio
images = [bluefinal, redfinal, greenfinal]# here read all images
imageio.mimsave("result.gif", images, 'GIF', duration = 0.2)

k = cv2.waitKey(0)
if k == ord("s"):
	cv2.destroyAllWindows()